"""
Support Handler
"""

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def support_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /support command"""
    
    support_text = (
        "💬 <b>Customer Support</b>\n\n"
        "We're here to help! Choose an option below:\n\n"
        "📧 Email: support@toolorax.com\n"
        "💬 Live Chat: Available 24/7\n"
        "📞 Call: +1-XXX-XXX-XXXX"
    )
    
    buttons = [
        [InlineKeyboardButton("📝 Create Ticket", callback_data="create_support_ticket")],
        [InlineKeyboardButton("❓ FAQ", callback_data="faq")]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.message.reply_text(
        support_text,
        reply_markup=reply_markup,
        parse_mode="HTML"
    )
