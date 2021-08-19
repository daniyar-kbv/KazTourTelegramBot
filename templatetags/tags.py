from django import template
from bot.utils.bot_modes import get_voice_mode

register = template.Library()


@register.simple_tag()
def voice_recognition_enabled():
    return get_voice_mode()


