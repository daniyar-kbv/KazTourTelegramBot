from main.models import TelegramUser, SurveyQuestion, QuestionAnswer, BotText
from bot.settings import bot
from bot.utils import keyboard, messages
from bot.steps import contacts
from telebot import types
import constants


def send_question(user: TelegramUser):
    try:
        question = SurveyQuestion.objects.get(my_order=user.current_sub_step)
    except:
        return
    markup = keyboard.create_survey_keyboard(question)
    bot.send_message(user.id, text=question.text, reply_markup=markup)


def start_survey(user: TelegramUser):
    user.current_step = constants.STEP_SURVEY
    user.current_sub_step = 1
    user.save()
    send_question(user)


def handle_survey(message: types.Message, user: TelegramUser):
    try:
        QuestionAnswer.objects.get(question__my_order=user.current_sub_step, text=message.text, is_own_option=True)
        user.current_micro_step = constants.MICRO_STEP_OWN_OPTION
        user.save()
        messages.send_messages([constants.TEXT_OWN_OPTION], user)
    except:
        if user.current_sub_step == 1:
            user.create_data(message.text)
        else:
            user.append_data(message.text)
        user.current_micro_step = None
        if user.current_sub_step != SurveyQuestion.objects.count():
            user.current_sub_step += 1
            user.save()
            send_question(user)
        else:
            user.current_sub_step = None
            user.save()
            contacts.start_contacts(message, user)

