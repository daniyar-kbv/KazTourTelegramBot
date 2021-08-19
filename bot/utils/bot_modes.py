from typing import Optional
from main.models import BotMode
import constants


def get_voice_mode() -> bool:
    mode: Optional[BotMode] = BotMode.get_mode_of_type(constants.BOT_MODE_VOICE_RECOGNITION)
    if mode:
        return mode.is_enabled
    return False


def set_voice_mode(is_enabled: bool):
    mode: Optional[BotMode] = BotMode.get_mode_of_type(constants.BOT_MODE_VOICE_RECOGNITION)
    if mode:
        mode.is_enabled = is_enabled
        mode.save()
