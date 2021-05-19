from celery import shared_task
from main.models import TelegramUser
from main.serializers import TelegramUserSerializer
import requests
import constants
import os


@shared_task
def start_bot():
    from bot.settings import bot
    bot.polling()


@shared_task()
def send_crm_data(user_id):
    try:
        user = TelegramUser.objects.get(id=user_id)
    except:
        return
    serializer = TelegramUserSerializer(user)
    print(serializer.data)
    response = requests.post(url=f'{constants.KAZTOUR_CRM_URL}?crm_verify_token={os.environ.get("CRM_VERIFY_TOKEN")}',
                             json=serializer.data)