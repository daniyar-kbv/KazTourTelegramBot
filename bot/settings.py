from bot.utils.start import start
from utils.recognizer import Recognizer
import telebot
import os

bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))
recognizer = Recognizer(bot=bot)

start(bot=bot)


