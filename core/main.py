from decouple import config

# SECURITY WARNING: keep the TOKEN used in production secret!
TOKEN = config("TOKEN", cast=str)


import asyncio

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(token=TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=["help", "start"])
async def send_welcome(message) -> None:
    text = "Hi, I am EchoBot.\nJust write me something and I will repeat it!"
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message) -> None:
    await bot.reply_to(message, message.text)


asyncio.run(bot.polling())
