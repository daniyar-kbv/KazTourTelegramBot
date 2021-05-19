from main.models import TelegramUser
import telebot


def auth_user(message: telebot.types.Message) -> TelegramUser:
    try:
        user = TelegramUser.objects.get(id=message.from_user.id)
        if message.from_user.username:
            user.username = message.from_user.username
        if message.from_user.first_name:
            user.first_name = message.from_user.first_name
        if message.from_user.last_name:
            user.last_name = message.from_user.last_name
        user.save()
    except:
        user = TelegramUser.objects.create(
            id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
    return user
