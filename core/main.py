import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from core.configs import messages, settings
from core.configs.settings import BOT, LOGGER
from core.decorators.memberships import is_in_channel
from core.decorators.throttlings import throttled

bot = BOT
logger = LOGGER


@bot.message_handler(commands=["start"])
@is_in_channel
@throttled(rate_limit=settings.RATE_LIMIT["start_rate_limit"], command_name="start")
async def start_handler(message):
    text = messages.START_MESSAGE
    await bot.reply_to(message, text)
    logger.info("executed start_handler")


@bot.message_handler(commands=["help"])
@is_in_channel
@throttled(rate_limit=settings.RATE_LIMIT["help_rate_limit"], command_name="help")
async def help_handler(message):
    text = messages.HELP_MESSAGE
    await bot.reply_to(message, text)
    logger.info("executed help_handler")


if __name__ == "__main__":
    import asyncio

    asyncio.run(bot.polling())
