from rest_framework.views import APIView
from rest_framework.response import Response
from bot.settings import bot
import telebot


class TelegramBotView(APIView):
    def post(self, request, format=None):
        json_string = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return Response()