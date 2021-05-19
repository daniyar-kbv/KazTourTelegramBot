from main.models import SurveyQuestion
from telebot import types
import constants


def create_regular_keyboard(options: list):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for option in options:
        keyboard.add(types.KeyboardButton(option))
    return keyboard


def create_grid_keyboard(options: list):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for index in range(0, len(options), 2):
        buttons = list(map(lambda option: types.KeyboardButton(option), options[index:index+2]))
        keyboard.row(*buttons)
    return keyboard


def create_survey_keyboard(question: SurveyQuestion):
    return create_grid_keyboard(list(map(lambda option: option.text, question.options.all())))