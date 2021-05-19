from main.models import TelegramUser, SurveyQuestion, ContactType, BotText
from bot.settings import bot
from bot.utils import messages
from telebot import types
import constants


def send_invalid(user: TelegramUser, invalid_type: int):
    if invalid_type == constants.INVALID_TYPE_DEFAULT:
        messages.send_messages([constants.TEXT_INVALID_RESPONSE], user)
    elif invalid_type == constants.INVALID_TYPE_PHONE:
        messages.send_messages([constants.TEXT_PHONE_NUMBER_INVALID], user)


def is_phone_number(text: str):
    for char in text:
        if char not in '+1234567890':
            return False
    return len(text) == 12 and text[0] == '+' and text[1] == '7'


def validate_greeting(message: types.Message):
    return message.text in [BotText.get_text(constants.TEXT_GREENING_OPTION_1),
                            BotText.get_text(constants.TEXT_GREENING_OPTION_2)]


def validate_contact_type(message: types.Message):
    return message.text in list(map(lambda contact_type: contact_type.text, ContactType.objects.all()))


def validate_audio_or_text(message: types.Message, user: TelegramUser):
    if user.current_sub_step == constants.SUB_STEP_AUDIO_ACCEPT:
        return message.text in [BotText.get_text(constants.TEXT_AUDIO_YES),
                                BotText.get_text(constants.TEXT_AUDIO_NO)]
    else:
        return True


def validate_survey(message: types.Message, user: TelegramUser):
    try:
        question = SurveyQuestion.objects.get(my_order=user.current_sub_step)
    except:
        return False
    if user.current_micro_step != constants.MICRO_STEP_OWN_OPTION:
        return message.text in list(map(lambda option: option.text, question.options.all()))
    return True


def validate(message: types.Message, user: TelegramUser):
    is_valid = None
    invalid_type = constants.INVALID_TYPE_DEFAULT
    if user.current_step == constants.STEP_GREETING:
        is_valid = validate_greeting(message)
    elif user.current_step == constants.STEP_CONTACT_TYPE:
        is_valid = validate_contact_type(message)
    elif user.current_step == constants.STEP_PHONE_NUMBER:
        is_valid = is_phone_number(message.text)
        invalid_type = constants.INVALID_TYPE_PHONE
    elif user.current_step == constants.STEP_AUDIO_OR_TEXT:
        is_valid = validate_audio_or_text(message, user)
    elif user.current_step == constants.STEP_SURVEY:
        is_valid = validate_survey(message, user)
    else:
        return False

    if not is_valid:
        send_invalid(user, invalid_type)
    return is_valid



