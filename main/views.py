from rest_framework.views import APIView
from rest_framework.response import Response
from main.serializers import VoiceRecoginitionSerializer
from bot.settings import bot
from bot.utils.bot_modes import set_voice_mode
import telebot


class TelegramBotView(APIView):
    def post(self, request, format=None):
        json_string = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return Response()


class SetVoiceRecognition(APIView):
    def post(self, request, format=None):
        serializer = VoiceRecoginitionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        set_voice_mode(serializer.data.get('enabled'))
        return Response()