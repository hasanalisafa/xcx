from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Define the token
TOKEN = 'YOUR_BOT_TOKEN'

async def start(update: Update, context: CallbackContext) -> None:
    """Handler for /start command"""
    await update.message.reply_text('Bot is responding!')

def main():
    """Main function to start the bot"""
    # Create the Application and use `Application.builder()` for the latest API
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))

    # Start polling for updates
    application.run_polling()

if __name__ == '__main__':
    main()