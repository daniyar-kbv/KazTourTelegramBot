from rest_framework import serializers
from main.models import TelegramUser


class TelegramUserSerializer(serializers.ModelSerializer):
    telegram_username = serializers.SerializerMethodField()
    answers = serializers.SerializerMethodField()
    contact_type = serializers.SerializerMethodField()

    class Meta:
        model = TelegramUser
        fields = ['telegram_username', 'first_name', 'last_name', 'answers', 'contact_type', 'phone_number']

    def get_telegram_username(self, obj):
        return obj.username

    def get_answers(self, obj):
        return obj.get_last_data().answers

    def get_contact_type(self, obj):
        return obj.get_last_data().contact_type


class VoiceRecoginitionSerializer(serializers.Serializer):
    enabled = serializers.BooleanField()