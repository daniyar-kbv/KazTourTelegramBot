# TELEGRAM_BOT_URL = 'https://telegram-bot.kaztour.kz/main/bot/'
TELEGRAM_BOT_URL = 'https://api.24goalsapp.com/bot_test/main/bot/'

STEP_GREETING = 1
STEP_AUDIO_OR_TEXT = 2
STEP_SURVEY = 3
STEP_CONTACT_TYPE = 4
STEP_PHONE_NUMBER = 5
STEP_END = 6

STEPS_ALL = [
    (STEP_GREETING, 'Приветсвие'),
    (STEP_AUDIO_OR_TEXT, 'Аудио или текст'),
    (STEP_SURVEY, 'Опрос'),
    (STEP_CONTACT_TYPE, 'Способ контакта'),
    (STEP_PHONE_NUMBER, 'Номер телефона')
]

SUB_STEP_AUDIO_START = 1
SUB_STEP_AUDIO_ACCEPT = 2

MICRO_STEP_OWN_OPTION = 1

TEXT_GREENING_1 = 1
TEXT_GREENING_2 = 2
TEXT_GREENING_3 = 3
TEXT_GREENING_4 = 4
TEXT_GREENING_OPTION_1 = 5
TEXT_GREENING_OPTION_2 = 6
TEXT_AUDIO_OR_TEXT = 7
TEXT_AUDIO_SUGGESTION = 8
TEXT_AUDIO_YES = 9
TEXT_AUDIO_NO = 10
TEXT_AUDIO_RETRY = 11
TEXT_CONTACT_TYPE_1 = 12
TEXT_CONTACT_TYPE_2 = 13
TEXT_PHONE_NUMBER = 14
TEXT_PHONE_NUMBER_INVALID = 15
TEXT_LAST = 16
TEXT_INVALID_RESPONSE = 17
TEXT_OWN_OPTION = 18

TEXT_ALL = [
    (TEXT_GREENING_1, 'Приветствие (1-е сообщение, должно содержать "{}" для вствки имени)'),
    (TEXT_GREENING_2, 'Приветствие (2-е сообщение)'),
    (TEXT_GREENING_3, 'Приветствие (3-е сообщение)'),
    (TEXT_GREENING_4, 'Приветствие (4-е сообщение)'),
    (TEXT_GREENING_OPTION_1, 'Вариант ответа 1 (после приветствия)'),
    (TEXT_GREENING_OPTION_2, 'Вариант ответа 2 (после приветствия)'),
    (TEXT_AUDIO_OR_TEXT, 'Текст о предложении отправить аудио'),
    (TEXT_AUDIO_SUGGESTION, 'Текст о подтверждении текста с аудио (должно содержать "{}" для вствки текста)'),
    (TEXT_AUDIO_YES, 'Вариант ответа 1 (подтверждение)'),
    (TEXT_AUDIO_NO, 'Вариант ответа 2 (опровержение)'),
    (TEXT_AUDIO_RETRY, 'Текст переотправки аудио'),
    (TEXT_CONTACT_TYPE_1, 'Текст о способе контакта (1-е сообщение, должно содержать "{}" для вствки имени)'),
    (TEXT_CONTACT_TYPE_2, 'Текст о способе контакта (2-е сообщение)'),
    (TEXT_PHONE_NUMBER, 'Текст об отправке номера телефона (шаблон)'),
    (TEXT_PHONE_NUMBER_INVALID, 'Текст о некорректном номере телефона'),
    (TEXT_LAST, 'Заключающее сообщение'),
    (TEXT_INVALID_RESPONSE, 'Текст ответа на некорректное сообщение'),
    (TEXT_OWN_OPTION, 'Текст сообщения (ввести свой вариант)')
]

INVALID_TYPE_DEFAULT = 1
INVALID_TYPE_PHONE = 2

KAZTOUR_CRM_URL = "https://crm.kaztour.kz/integrations/telegram/lead-bot/"
