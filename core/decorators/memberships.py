from functools import wraps

from telebot.types import Message

from core.configs import settings
from core.configs.settings import BOT, LOGGER

logger = LOGGER
bot = BOT


def is_in_channel(func):
    """Decorator for checking membership in a channel."""

    @wraps(func)
    async def wrapper(message: Message, *args, **kwargs):
        user_id = message.from_user.id

        try:
            chat_member = await bot.get_chat_member(settings.CHANNEL_ID, user_id)
            if chat_member.status in ["member", "administrator", "creator"]:
                return await func(message, *args, **kwargs)
            else:
                await bot.reply_to(
                    message,
                    text=f"❗️ Please join our channel {settings.CHANNEL_LINK} to use this bot.",
                )
                return None
        except Exception as e:
            logger.error(f"Error checking user membership: {e}")
            await bot.reply_to(
                message,
                text="❌ Could not verify your membership in the channel. Please try again.",
            )
            return None

    return wrapper
