from main.models import TelegramUser, ContactType, BotText
from bot.settings import bot
from bot.utils import keyboard, messages
from bot.steps import phone_number
from telebot import types
import constants


def start_contacts(message: types.Message, user: TelegramUser):
    user.current_step = constants.STEP_CONTACT_TYPE
    user.save()
    markup = keyboard.create_grid_keyboard(ContactType.get_texts())
    messages.send_messages([constants.TEXT_CONTACT_TYPE_1, constants.TEXT_CONTACT_TYPE_2], user, markup)


def handle_contacts(message: types.Message, user: TelegramUser):
    user_data = user.get_last_data()
    user_data.contact_type = message.text
    user_data.save()
    phone_number.start_phone_number(message, user)

