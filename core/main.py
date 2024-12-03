import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from core.decorators.memberships import is_in_channel
from core.settings import BOT

bot = BOT


@bot.message_handler(commands=["start"])
@is_in_channel
async def start_handler(message):
    text = "Hi, I am EchoBot.\nJust write me something and I will repeat it!"
    await bot.reply_to(message, text)


if __name__ == "__main__":
    import asyncio

    asyncio.run(bot.polling())
