from django.conf import settings
from telebot import TeleBot
from main.tasks import start_bot
import constants


def start(bot: TeleBot):
    if settings.DEBUG:
        start_bot.delay()
    else:
        try:
            bot.set_webhook(url=constants.TELEGRAM_BOT_URL)
        except:
            pass