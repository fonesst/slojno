import subprocess
from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater

# Function to install TDLib API automatically
def install_telegram_bot_api():
    subprocess.run(["pip", "install", "telegram-bot-api"])

# Install telegram-bot-api without cloning the repo
install_telegram_bot_api()

# Your Telegram Bot Token
API_TOKEN = '7368730334:AAH9xUG8G_Ro8mvV_fDQxd5ddkwjxHnBoeg'

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
    main()
