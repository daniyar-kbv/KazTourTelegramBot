from django.urls import path
from main.views import TelegramBotView, SetVoiceRecognition

urlpatterns = [
    path('bot/', TelegramBotView.as_view()),
    path('voice/', SetVoiceRecognition.as_view(), name='voice')
]
