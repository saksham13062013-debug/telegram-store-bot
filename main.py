#!/usr/bin/env python3
"""
Telegram Store Bot - Main Entry Point
"""

import logging
from app.config import BOT_TOKEN, ADMIN_USER_ID
from app.database import init_db
from app.handlers.start import start_handler
from app.handlers.products import products_handler
from app.handlers.cart import cart_handler
from app.handlers.orders import orders_handler
from app.handlers.wallet import wallet_handler
from app.handlers.support import support_handler
from app.handlers.admin import admin_handler
from app.handlers.callbacks import callback_handler

from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Start the bot."""
    # Initialize database
    init_db()
    logger.info("Database initialized")
    
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", start_handler))
    application.add_handler(CommandHandler("products", products_handler))
    application.add_handler(CommandHandler("cart", cart_handler))
    application.add_handler(CommandHandler("orders", orders_handler))
    application.add_handler(CommandHandler("wallet", wallet_handler))
    application.add_handler(CommandHandler("support", support_handler))
    application.add_handler(CommandHandler("admin", admin_handler))
    
    # Add message handler for text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, callback_handler))
    
    # Add callback query handler
    application.add_handler(CallbackQueryHandler(callback_handler))
    
    # Start the Bot
    logger.info("Starting bot...")
    application.run_polling(allowed_updates=["message", "callback_query"])

if __name__ == '__main__':
    main()
