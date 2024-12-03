import logging

import telebot
from decouple import config
from telebot.async_telebot import AsyncTeleBot

TOKEN = config("TOKEN", cast=str)

BOT = AsyncTeleBot(token=TOKEN)


logger = telebot.logger
logger.setLevel(logging.INFO)
LOGGER = logger

CHANNEL_ID = config("CHANNEL_ID", cast=str)
CHANNEL_LINK = config("CHANNEL_LINK", cast=str)

RATE_LIMIT = {"start_rate_limit": 20}
