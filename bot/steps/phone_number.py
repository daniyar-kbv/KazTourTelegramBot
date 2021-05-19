from main.models import TelegramUser, BotText
from bot.settings import bot
from bot.utils import keyboard, messages
from telebot import types
import constants


def start_phone_number(message: types.Message, user: TelegramUser):
    user.current_step = constants.STEP_PHONE_NUMBER
    user.save()
    messages.send_messages([constants.TEXT_PHONE_NUMBER], user)


def handle_phone_number(message: types.Message, user: TelegramUser):
    user.phone_number = message.text
    user.current_step = constants.STEP_END
    user.save()
    user.finish_data()
    messages.send_messages([constants.TEXT_LAST], user)
