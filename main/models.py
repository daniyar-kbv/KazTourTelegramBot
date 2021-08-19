from django.db import models
from django.db import connection
from django.conf import settings
from typing import Optional
from utils.general import get_choice_value
import constants
import datetime


class OrderedModel(models.Model):
    my_order = models.PositiveIntegerField('Сортировка', default=0, blank=False, null=False)

    class Meta:
        ordering = ['my_order']
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.my_order == 0:
            largest_order = self.__class__.objects.order_by('-my_order').first()
            if largest_order:
                self.my_order = largest_order.my_order + 1
            else:
                self.my_order = 1
        super(OrderedModel, self).save(force_insert, force_update, using, update_fields)


class TelegramUser(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField('Имя', max_length=100, null=True, blank=True)
    last_name = models.CharField('Фамилия', max_length=100, null=True, blank=True)
    phone_number = models.CharField('Номер телефона', max_length=12, null=True, blank=True)
    current_step = models.PositiveSmallIntegerField('Текущий шаг', default=constants.STEP_GREETING, choices=constants.STEPS_ALL)
    current_sub_step = models.PositiveSmallIntegerField('Текущий подшаг', null=True, blank=True)
    current_micro_step = models.PositiveSmallIntegerField('Текущий микро шаг', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь Telegram'
        verbose_name_plural = 'Пользователи Telegram'

    def __str__(self):
        return self.username

    def get_name(self):
        if self.first_name:
            return self.first_name
        return self.username

    def create_data(self, data_text):
        UserData.objects.create(user=self, answers=data_text)

    def append_data(self, data_text):
        last_data = UserData.objects.filter(user=self).last()
        if last_data and not last_data.end_date:
            last_data.answers = last_data.answers + f'\n{data_text}'
            last_data.save()

    def finish_data(self):
        from main.tasks import send_crm_data
        last_data = UserData.objects.filter(user=self).last()
        if last_data and not last_data.end_date:
            last_data.end_date = datetime.datetime.now()
            last_data.save()
        if settings.DEBUG:
            send_crm_data(self.id)
        else:
            send_crm_data.delay(self.id)

    def add_audio(self, data_text):
        last_data = UserData.objects.filter(user=self).last()
        if last_data:
            last_data.audio_suggestion = data_text
            last_data.save()
        else:
            UserData.objects.create(user=self, audio_suggestion=data_text)

    def get_last_audio_text(self):
        last_data = UserData.objects.filter(user=self).last()
        if last_data:
            return last_data.audio_suggestion

    def get_last_data(self):
        return UserData.objects.filter(user=self).last()


class UserData(models.Model):
    user = models.ForeignKey(
        TelegramUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь телеграм',
        related_name='datas',
    )
    contact_type = models.CharField('Способ контакта', max_length=100, null=True)
    answers = models.TextField('Текст', null=True, blank=True)
    audio_suggestion = models.TextField('Переведенное аудио', null=True, blank=True)
    start_date = models.DateTimeField('Дата начала', auto_now_add=True)
    end_date = models.DateTimeField('Дата окончания', null=True, blank=True)

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователя'

    def __str__(self):
        return f'{self.user.username}: {self.start_date}'


class SurveyQuestion(OrderedModel):
    text = models.TextField('Текст')

    class Meta(OrderedModel.Meta):
        verbose_name = 'Вопрос опроса'
        verbose_name_plural = 'Вопросы опроса'

    def __str__(self):
        return self.text


class QuestionAnswer(OrderedModel):
    question = models.ForeignKey(
        SurveyQuestion,
        on_delete=models.CASCADE,
        verbose_name='Вопрос',
        related_name='options',
        null=True
    )
    text = models.TextField('Текст')
    is_own_option = models.BooleanField('Свой вариант', default=False)

    class Meta(OrderedModel.Meta):
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопрос'

    def __str__(self):
        return self.text


class BotText(OrderedModel):
    id = models.PositiveSmallIntegerField(primary_key=True, choices=constants.TEXT_ALL)
    text = models.TextField('Текст', null=True, blank=True)

    class Meta(OrderedModel.Meta):
        verbose_name = 'Текст бота'
        verbose_name_plural = 'Текста бота'

    def __str__(self):
        return get_choice_value(self.id, constants.TEXT_ALL)

    @staticmethod
    def get_text(key: int) -> Optional[str]:
        try:
            bot_text = BotText.objects.get(id=key)
            return bot_text.text
        except:
            return None


class ContactType(OrderedModel):
    text = models.CharField('Надпись', max_length=100)

    class Meta(OrderedModel.Meta):
        verbose_name = 'Способ связи'
        verbose_name_plural = 'Способы связи'

    def __str__(self):
        return self.text

    @staticmethod
    def get_texts() -> list:
        return list(map(lambda contact_type: contact_type.text, ContactType.objects.all()))


class BotMode(models.Model):
    type = models.PositiveSmallIntegerField('Тип',
                                            choices=constants.BOT_MODES,
                                            null=False,
                                            blank=False)
    is_enabled = models.BooleanField('Включен',
                                     default=False)

    class Meta:
        verbose_name = 'Режим бота'
        verbose_name_plural = 'Режимы бота'

    def __str__(self):
        return get_choice_value(self.type, constants.BOT_MODES)

    @staticmethod
    def get_mode_of_type(type: int):
        mode = None
        try:
            mode = BotMode.objects.get(type=type)
        except:
            pass
        return mode



class DefaultDataManager:
    @staticmethod
    def create_default_data():
        DefaultDataManager._create_bot_texts()
        DefaultDataManager._create_contact_types()
        DefaultDataManager._create_questions()
        DefaultDataManager._create_modes()

    @staticmethod
    def _create_bot_texts():
        if 'main_bottext' in connection.introspection.table_names():
            for index, text in enumerate(constants.TEXT_ALL):
                try:
                    BotText.objects.get(id=text[0])
                except:
                    obj: BotText = BotText.objects.create(id=text[0])
                    obj.text = get_choice_value(text[0], constants.DEFAULT_TEXT_ALL)
                    obj.save()

    @staticmethod
    def _create_contact_types():
        if 'main_contacttype' in connection.introspection.table_names() and \
                ContactType.objects.count() == 0:
            for index, contact in enumerate(constants.DEFAULT_CONTACT_TYPES):
                contact: ContactType = ContactType.objects.create(text=contact)
                contact.save()

    @staticmethod
    def _create_questions():
        if 'main_surveyquestion' in connection.introspection.table_names() and \
                SurveyQuestion.objects.count() == 0:
            question = SurveyQuestion.objects.create(text=constants.DEFAULT_QUESTION)
            for index, answer_text in enumerate(constants.DEFAULT_ANSWERS):
                answer = QuestionAnswer.objects.create(question=question, text=answer_text)
                if answer_text == constants.DEFAULT_ANSWER_4:
                    answer.is_own_option = True
                answer.save()

    @staticmethod
    def _create_modes():
        if 'main_botmode' in connection.introspection.table_names() and \
                BotMode.objects.count() == 0:
            for index, mode in enumerate(constants.BOT_MODES):
                try:
                    BotMode.objects.get(type=mode[0])
                except:
                    BotMode.objects.create(type=mode[0])


DefaultDataManager.create_default_data()