from telebot import TeleBot
from main.tasks import start_bot
import constants


def start(bot: TeleBot, debug: bool):
    if debug:
        start_bot.delay()
    else:
        try:
            bot.set_webhook(url=constants.TELEGRAM_BOT_URL)
        except:
            pass