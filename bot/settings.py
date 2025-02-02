from bot.utils.start import start
from utils.recognizer import Recognizer
import telebot
import os

BOT_DEBUG = bool(int(os.environ.get('BOT_DEBUG', default=0)))
bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))
recognizer = Recognizer(bot=bot)

start(bot=bot, debug=BOT_DEBUG)


