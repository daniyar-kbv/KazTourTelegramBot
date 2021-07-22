TELEGRAM_BOT_URL = 'https://telegram-bot.kaztour.kz/main/bot/'

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
    (TEXT_AUDIO_OR_TEXT, 'Текст с предложением отправить аудио'),
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

DEFAULT_TEXT_GREENING_1 = 'Привет, {}! Спасибо что обратились к виртуальному помощнику "KAZTOUR"'
DEFAULT_TEXT_GREENING_2 = 'Ответьте на 5 вопросов о путешествии и менеджер индивидуально подберет для вас тур👍'
DEFAULT_TEXT_GREENING_3 = 'Или отправьте нам аудио или текст с вашими пожеланиями! На пример: "Хочу поехать в египет ' \
                          'с семьей в следующем месяце на неделю"'
DEFAULT_TEXT_GREENING_4 = 'Выберите опцию👇'
DEFAULT_TEXT_GREENING_OPTION_1 = 'Пройти опрос'
DEFAULT_TEXT_GREENING_OPTION_2 = 'Отправить аудио/текст'
DEFAULT_TEXT_AUDIO_OR_TEXT = 'Отправьте нам аудио или текст с вашими пожеланиями'
DEFAULT_TEXT_AUDIO_SUGGESTION = 'Вы сказали: "{}"?'
DEFAULT_TEXT_AUDIO_YES = 'Да'
DEFAULT_TEXT_AUDIO_NO = 'Нет'
DEFAULT_TEXT_AUDIO_RETRY = 'Отправьте аудио или текст еще раз'
DEFAULT_TEXT_CONTACT_TYPE_1 = '{}, спасибо за ответы! Ваша заявка сформирована и будет отправлена менеджеру!'
DEFAULT_TEXT_CONTACT_TYPE_2 = 'Как с вами связаться👇'
DEFAULT_TEXT_PHONE_NUMBER = 'Напишите номер в формате +77771112233'
DEFAULT_TEXT_PHONE_NUMBER_INVALID = 'Номер введен некорректно. Напишите его в виде +7 и 10 цифр подряд. Пример ' \
                                    '+77771112233'
DEFAULT_TEXT_LAST = 'Спасибо! Скоро с вами свяжется менеджер, подтвердит заявку и сделает подборку туров.'
DEFAULT_TEXT_INVALID_RESPONSE = 'Выберите вариант с клавиатуры внизу'
DEFAULT_TEXT_OWN_OPTION = 'Введите свой вариант👇'

DEFAULT_TEXT_ALL = [
    (TEXT_GREENING_1, DEFAULT_TEXT_GREENING_1),
    (TEXT_GREENING_2, DEFAULT_TEXT_GREENING_2),
    (TEXT_GREENING_3, DEFAULT_TEXT_GREENING_3),
    (TEXT_GREENING_4, DEFAULT_TEXT_GREENING_4),
    (TEXT_GREENING_OPTION_1, DEFAULT_TEXT_GREENING_OPTION_1),
    (TEXT_GREENING_OPTION_2, DEFAULT_TEXT_GREENING_OPTION_2),
    (TEXT_AUDIO_OR_TEXT, DEFAULT_TEXT_AUDIO_OR_TEXT),
    (TEXT_AUDIO_SUGGESTION, DEFAULT_TEXT_AUDIO_SUGGESTION),
    (TEXT_AUDIO_YES, DEFAULT_TEXT_AUDIO_YES),
    (TEXT_AUDIO_NO, DEFAULT_TEXT_AUDIO_NO),
    (TEXT_AUDIO_RETRY, DEFAULT_TEXT_AUDIO_RETRY),
    (TEXT_CONTACT_TYPE_1, DEFAULT_TEXT_CONTACT_TYPE_1),
    (TEXT_CONTACT_TYPE_2, DEFAULT_TEXT_CONTACT_TYPE_2),
    (TEXT_PHONE_NUMBER, DEFAULT_TEXT_PHONE_NUMBER),
    (TEXT_PHONE_NUMBER_INVALID, DEFAULT_TEXT_PHONE_NUMBER_INVALID),
    (TEXT_LAST, DEFAULT_TEXT_LAST),
    (TEXT_INVALID_RESPONSE, DEFAULT_TEXT_INVALID_RESPONSE),
    (TEXT_OWN_OPTION, DEFAULT_TEXT_OWN_OPTION)
]

DEFAULT_CONTACT_TYPE_1 = 'Позвонить'
DEFAULT_CONTACT_TYPE_2 = 'WhatsApp'
DEFAULT_CONTACT_TYPE_3 = 'Telegram'

DEFAULT_CONTACT_TYPES = [DEFAULT_CONTACT_TYPE_1, DEFAULT_CONTACT_TYPE_2, DEFAULT_CONTACT_TYPE_3]

DEFAULT_QUESTION = 'В какой стране вы хотите побывать?🌍'
DEFAULT_ANSWER_1 = 'Египет'
DEFAULT_ANSWER_2 = 'Турция'
DEFAULT_ANSWER_3 = 'ОАЭ'
DEFAULT_ANSWER_4 = 'Другая страна'

DEFAULT_ANSWERS = [DEFAULT_ANSWER_1, DEFAULT_ANSWER_2, DEFAULT_ANSWER_3, DEFAULT_ANSWER_4]

INVALID_TYPE_DEFAULT = 1
INVALID_TYPE_PHONE = 2

KAZTOUR_CRM_URL = "https://crm.kaztour.kz/integrations/telegram/lead-bot/"

FILE_NAME = 'audio'
SRC_EXTENSION = 'opus'

YANDEX_BUCKET_NAME = 'tui-bucket'
YANDEX_RECOGNITION_SHORT_AUDIO_URL = 'https://stt.api.cloud.yandex.net/speech/v1/stt:recognize'
YANDEX_RECOGNITION_LONG_AUDIO_URL = 'https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize'
YANDEX_RECOGNITION_RESULTS_URL = 'https://operation.api.cloud.yandex.net/operations/{operation_id}'
YANDEX_STORAGE_BUCKET_URL = 'https://storage.yandexcloud.net/{bucket_name}/{file_path}'