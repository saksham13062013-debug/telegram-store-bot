"""
Admin Handler
"""

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from app.config import ADMIN_USER_ID

async def admin_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /admin command"""
    
    user_id = update.effective_user.id
    
    # Check if user is admin
    if user_id != ADMIN_USER_ID:
        await update.message.reply_text(
            "❌ You don't have permission to access the admin panel."
        )
        return
    
    admin_text = (
        "🔧 <b>Admin Panel</b>\n\n"
        "Manage your store here:"
    )
    
    buttons = [
        [InlineKeyboardButton("📦 Manage Products", callback_data="admin_products")],
        [InlineKeyboardButton("📊 Orders", callback_data="admin_orders")],
        [InlineKeyboardButton("👥 Users", callback_data="admin_users")],
        [InlineKeyboardButton("📈 Analytics", callback_data="admin_analytics")],
        [InlineKeyboardButton("🔔 Send Alert", callback_data="admin_alert")]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.message.reply_text(
        admin_text,
        reply_markup=reply_markup,
        parse_mode="HTML"
    )
