from telebot import types
from main.models import TelegramUser, BotText
from bot.settings import bot
from bot.utils import keyboard, validation, messages
from bot.steps import survey, audio_text
import constants
import time


def send_greetings(message: types.Message, user: TelegramUser):
    markup = keyboard.create_regular_keyboard([BotText.get_text(constants.TEXT_GREENING_OPTION_1),
                                               BotText.get_text(constants.TEXT_GREENING_OPTION_2)])
    messages.send_messages([constants.TEXT_GREENING_1,
                            constants.TEXT_GREENING_2,
                            constants.TEXT_GREENING_3,
                            constants.TEXT_GREENING_4],
                           user,
                           markup)


def handle_greeting(message: types.Message, user: TelegramUser):
    if message.text == BotText.get_text(constants.TEXT_GREENING_OPTION_1):
        survey.start_survey(user)
    elif message.text == BotText.get_text(constants.TEXT_GREENING_OPTION_2):
        audio_text.start_audio(user)
