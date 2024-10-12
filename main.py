import os
import asyncio
from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater
from td.client import Client

# Your Telegram Bot Token
API_TOKEN = '7368730334:AAH9xUG8G_Ro8mvV_fDQxd5ddkwjxHnBoeg'

# Initialize TDLib client
async def init_tdlib():
    tdlib_path = "/usr/local/lib/libtdjson.so"  # Update this path to your system's tdjson location
    td_client = Client(tdlib_path)
    await td_client.connect()
    return td_client

# Greeting function
def start(update: Update, context):
    user_first_name = update.message.chat.first_name
    update.message.reply_text(f"Hello, {user_first_name}! Welcome to the bot!")

# Main function to handle bot setup
def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Start command to greet users
    dp.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_tdlib())
    main()
