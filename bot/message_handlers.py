from main.models import BotText
from bot.settings import bot
from bot.utils import keyboard, auth, validation
from bot.steps import greeting, audio_text, contacts, survey, phone_number
import constants


@bot.message_handler(commands=['start', 'restart'])
def handle_start(message):
    user = auth.auth_user(message)
    user.current_step = constants.STEP_GREETING
    user.save()
    greeting.send_greetings(message, user)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    user = auth.auth_user(message)
    if validation.validate(message, user):
        if user.current_step == constants.STEP_GREETING:
            greeting.handle_greeting(message, user)
        elif user.current_step == constants.STEP_AUDIO_OR_TEXT:
            audio_text.handle_audio(message, user)
        elif user.current_step == constants.STEP_SURVEY:
            survey.handle_survey(message, user)
        elif user.current_step == constants.STEP_CONTACT_TYPE:
            contacts.handle_contacts(message, user)
        elif user.current_step == constants.STEP_PHONE_NUMBER:
            phone_number.handle_phone_number(message, user)


@bot.message_handler(content_types=['voice'])
def get_voice_messages(message):
    user = auth.auth_user(message)
    audio_text.handle_audio(message, user)

