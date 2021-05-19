from django.urls import path
from main.views import TelegramBotView

urlpatterns = [
    path('bot/', TelegramBotView.as_view())
]
