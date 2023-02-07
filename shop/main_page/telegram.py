from dotenv import load_dotenv
import os

from telegram.ext import CommandHandler, Updater, MessageHandler
from telegram import Bot

load_dotenv()

secret_token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=secret_token)


