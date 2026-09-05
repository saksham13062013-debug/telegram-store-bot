"""
Wallet Handler
"""

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from app.database import SessionLocal
from app.models.user import User
from app.config import CURRENCY

async def wallet_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /wallet command"""
    
    user_id = update.effective_user.id
    db = SessionLocal()
    
    # Get user wallet
    user = db.query(User).filter(User.user_id == user_id).first()
    
    if not user:
        await update.message.reply_text("❌ User not found.")
        db.close()
        return
    
    # Format wallet message
    wallet_text = f"💳 <b>Your Wallet</b>\n\n"
    wallet_text += f"Balance: {CURRENCY}{user.balance}\n"
    
    # Create buttons
    buttons = [
        [InlineKeyboardButton("➕ Add Money", callback_data="add_money")],
        [InlineKeyboardButton("💸 Withdraw", callback_data="withdraw")]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.message.reply_text(
        wallet_text,
        reply_markup=reply_markup,
        parse_mode="HTML"
    )
    
    db.close()
