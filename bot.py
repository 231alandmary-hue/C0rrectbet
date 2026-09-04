import os
import logging
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token from environment variable
BOT_TOKEN = os.environ.get('BOT_TOKEN')
if not BOT_TOKEN:
    logger.error("No BOT_TOKEN found in environment variables")
    sys.exit(1)

# Channel invite link
CHANNEL_LINK = "https://t.me/+QvCFEopP3r9hY2Q0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send welcome message when /start is issued."""
    try:
        welcome_message = (
            f"👋 Welcome!\n\n"
            f"Thanks for joining us. Tap the button below to access our Telegram channel."
        )
        
        # Create inline keyboard with join button
        keyboard = [
            [InlineKeyboardButton("🚀 Join Our Channel", url=CHANNEL_LINK)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            welcome_message,
            reply_markup=reply_markup
        )
        logger.info(f"Sent welcome message to user {update.effective_user.id}")
    except Exception as e:
        logger.error(f"Error in start handler: {e}")

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button callbacks (though not strictly needed since it's a URL button)."""
    try:
        query = update.callback_query
        await query.answer()
        logger.info(f"Button clicked by user {update.effective_user.id}")
    except Exception as e:
        logger.error(f"Error in button callback: {e}")

def main() -> None:
    """Start the bot."""
    try:
        logger.info("Starting bot...")
        logger.info(f"Bot token length: {len(BOT_TOKEN)}")
        
        # Create the Application
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Register handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(button_callback))
        
        # Start the Bot
        logger.info("Bot is ready and polling...")
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    except Exception as e:
        logger.error(f"Fatal error in main: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
