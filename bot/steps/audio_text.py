from main.models import TelegramUser, BotText
from bot.settings import bot, recognizer
from bot.steps import contacts
from bot.utils import messages, keyboard
from telebot import types
import constants
import time


def translate_to_text(message: types.Message):
    bot.send_chat_action(message.chat.id, 'typing')
    return recognizer.recognize_speech(message)


def start_audio(user: TelegramUser):
    user.current_step = constants.STEP_AUDIO_OR_TEXT
    user.current_sub_step = constants.SUB_STEP_AUDIO_START
    user.save()
    messages.send_messages([constants.TEXT_AUDIO_OR_TEXT], user)


def handle_audio(message: types.Message, user: TelegramUser):
    if user.current_sub_step == constants.SUB_STEP_AUDIO_START:
        if message.content_type == 'text':
            user.create_data(message.text)
            user.current_sub_step = None
            user.save()
            contacts.start_contacts(message, user)
        elif message.content_type == 'voice':
            user.current_sub_step = constants.SUB_STEP_AUDIO_ACCEPT
            user.save()
            translated_text = translate_to_text(message)
            user.add_audio(translated_text)
            markup = keyboard.create_regular_keyboard([BotText.get_text(constants.TEXT_AUDIO_YES),
                                                       BotText.get_text(constants.TEXT_AUDIO_NO)])
            messages.send_messages([constants.TEXT_AUDIO_SUGGESTION], user, markup)
    elif user.current_sub_step == constants.SUB_STEP_AUDIO_ACCEPT:
        if message.text == BotText.get_text(constants.TEXT_AUDIO_YES):
            user.create_data(user.get_last_audio_text())
            user.current_sub_step = None
            user.save()
            contacts.start_contacts(message, user)
        elif message.text == BotText.get_text(constants.TEXT_AUDIO_NO):
            user.current_sub_step = constants.SUB_STEP_AUDIO_START
            user.save()
            messages.send_messages([constants.TEXT_AUDIO_RETRY], user)


