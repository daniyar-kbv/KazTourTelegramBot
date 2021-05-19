from django.db import models
from django.db import connection
from django.contrib.auth.models import User
from django.conf import settings
from typing import Optional
from utils.general import get_choice_value
import constants
import datetime
import os


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
    answers = models.TextField('Текст')
    audio_suggestion = models.TextField('Переведенное аудио', null=True, blank=True)
    start_date = models.DateTimeField('Дата начала', auto_now_add=True)
    end_date = models.DateTimeField('Дата окончания', null=True, blank=True)

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователя'

    def __str__(self):
        return f'{self.user.username}: {self.start_date}'


class SurveyQuestion(models.Model):
    text = models.TextField('Текст')
    my_order = models.PositiveIntegerField('Сортировка', default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Вопрос опроса'
        verbose_name_plural = 'Вопросы опроса'
        ordering = ['my_order']

    def __str__(self):
        return self.text


class QuestionAnswer(models.Model):
    question = models.ForeignKey(
        SurveyQuestion,
        on_delete=models.CASCADE,
        verbose_name='Вопрос',
        related_name='options',
        null=True
    )
    text = models.TextField('Текст')
    is_own_option = models.BooleanField('Свой вариант', default=False)
    my_order = models.PositiveIntegerField('Сортировка', default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопрос'
        ordering = ['my_order']

    def __str__(self):
        return self.text


class BotText(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True, choices=constants.TEXT_ALL)
    text = models.TextField('Текст', null=True, blank=True)
    my_order = models.PositiveIntegerField('Сортировка', default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Текст бота'
        verbose_name_plural = 'Текста бота'
        ordering = ['my_order']

    def __str__(self):
        return get_choice_value(self.id, constants.TEXT_ALL)

    @staticmethod
    def get_text(key: int) -> Optional[str]:
        try:
            bot_text = BotText.objects.get(id=key)
            return bot_text.text
        except:
            return None


class ContactType(models.Model):
    text = models.CharField('Надпись', max_length=100)

    class Meta:
        verbose_name = 'Способ связи'
        verbose_name_plural = 'Способы связи'

    def __str__(self):
        return self.text

    @staticmethod
    def get_texts() -> list:
        return list(map(lambda contact_type: contact_type.text, ContactType.objects.all()))


if 'main_bottext' in connection.introspection.table_names():
    for index, text in enumerate(constants.TEXT_ALL):
        try:
            BotText.objects.get(id=text[0])
        except:
            obj = BotText.objects.create(id=text[0])
            obj.my_order = index
            obj.save()
