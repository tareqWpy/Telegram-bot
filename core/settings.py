import logging

from decouple import config
from telebot.async_telebot import AsyncTeleBot

TOKEN = config("TOKEN", cast=str)

BOT = AsyncTeleBot(token=TOKEN)

LOGGING = logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

CHANNEL_ID = config("CHANNEL_ID", cast=str)
CHANNEL_LINK = config("CHANNEL_LINK", cast=str)
