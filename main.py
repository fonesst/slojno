import os
import sys
import subprocess
import telebot
from telebot import types

# Автоматическая установка TDLib
try:
    import tdlib
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tdlib-python"])
    import tdlib

# Токен вашего бота
API_TOKEN = '7368730334:AAH9xUG8G_Ro8mvV_fDQxd5ddkwjxHnBoeg'

# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик для команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Привет, {message.from_user.first_name}! Добро пожаловать в нашего Telegram бота.")

# Запуск бота
if __name__ == "__main__":
    bot.infinity_polling()
