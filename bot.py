from telegram.ext import Updater, CommandHandler

# Replace with your actual Bot Token
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"

def start(update, context):
    update.message.reply_text("Hello! 👋 I am alive and working.")

def help_command(update, context):
    update.message.reply_text("Available commands:\n/start - Start the bot\n/help - Show this help")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Start polling
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
