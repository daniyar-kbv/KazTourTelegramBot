from main.models import TelegramUser, BotText
from bot.settings import bot
from telebot import types
import time
import constants

SLEEP_TIME = 1


def send_messages(texts: list, user: TelegramUser, markup: types.ReplyKeyboardMarkup = None):
    for index, text in enumerate(texts):
        bot_text = BotText.get_text(text)
        if text == constants.TEXT_GREENING_1:
            bot_text = bot_text.format(user.get_name())
        elif text == constants.TEXT_AUDIO_SUGGESTION:
            bot_text = bot_text.format(user.get_last_audio_text())
        elif text == constants.TEXT_CONTACT_TYPE_1:
            bot_text = bot_text.format(user.get_name())
        if index == len(texts) - 1 and markup:
            bot.send_message(user.id, bot_text, reply_markup=markup)
        else:
            bot.send_message(user.id, bot_text)
        time.sleep(SLEEP_TIME)