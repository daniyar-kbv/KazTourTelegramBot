from django.conf import settings
from main.tasks import start_bot
import telebot
import os
import constants

bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))


if settings.DEBUG:
    start_bot.delay()
else:
    try:
        bot.set_webhook(url=constants.TELEGRAM_BOT_URL)
    except:
        pass
