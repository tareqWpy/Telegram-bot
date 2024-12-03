import time
from collections import defaultdict
from functools import wraps

from core.configs.settings import BOT, LOGGER

bot = BOT
logger = LOGGER


throttle_storage = defaultdict(lambda: 0)


def throttled(rate_limit: int):
    """Decorator for throttling function calls."""

    def decorator(func):
        @wraps(func)
        async def wrapper(message, *args, **kwargs):
            user_id = message.from_user.id
            current_time = time.time()
            last_called = throttle_storage[user_id]

            if current_time - last_called < rate_limit:
                remaining_time = rate_limit - (current_time - last_called)
                await bot.reply_to(
                    message,
                    f"Please wait {int(remaining_time)} seconds before using this command again.",
                )
                logger.info(f"Throttled message from user: {user_id}")
                return

            throttle_storage[user_id] = current_time
            return await func(message, *args, **kwargs)

        return wrapper

    return decorator
