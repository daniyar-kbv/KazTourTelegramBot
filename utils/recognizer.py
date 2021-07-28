from typing import Optional
from telebot import TeleBot
from telebot.types import Message
from utils.storage_service import StorageService
from utils.recognition_service import RecognitionService
import os


class Recognizer:
    __storage_service = StorageService()
    __recognition_service = RecognitionService()
    __bot: TeleBot

    def __init__(self, bot: TeleBot):
        self.__bot = bot

    def recognize_speech(self, message: Message) -> Optional[str]:
        print('saving audio file')
        self.__save_audio(message)

        print(f'message.voice.duration: {message.voice.duration}')
        if message.voice.duration >= 30:
            print('long audio')
            text = self.__recognize_long_voice(message)
        else:
            print('short audio')
            text = self.__recognize_short_voice(message)

        print('deleting audio file')
        self.__delete_audio(message)

        return text

    def __recognize_short_voice(self, message: Message) -> Optional[str]:
        return self.__recognition_service.send_short_audio(self.__get_file_path(message))

    def __recognize_long_voice(self, message: Message) -> Optional[str]:
        self.__storage_service.upload_file(path=self.__get_file_path(message),
                                           name=self.__get_file_name(message))
        text = self.__recognition_service.send_long_audio(file_name=self.__get_file_name(message))
        self.__storage_service.delete_file(self.__get_file_name(message))
        return text

    def __get_audio(self, message: Message) -> bytes:
        print('getting file info')
        file_info = self.__bot.get_file(message.voice.file_id)
        print(f'file info: {file_info}')
        print('downloading file')
        return self.__bot.download_file(file_info.file_path)

    def __get_file_name(self, message: Message) -> str:
        return f'{message.chat.id}_{message.id}.ogg'

    def __get_file_path(self, message: Message) -> str:
        return f'tmp/{self.__get_file_name(message)}'

    def __save_audio(self, message: Message):
        print('getting audio file')
        downloaded_file = self.__get_audio(message)
        print('saving downloaded file')
        with open(f'{self.__get_file_path(message)}', 'wb') as new_file:
            new_file.write(downloaded_file)
        print(f'saved downloaded file to: {new_file}')

    def __delete_audio(self, message):
        os.system(f'rm {self.__get_file_path(message)}')
