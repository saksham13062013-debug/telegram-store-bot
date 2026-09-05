"""
Start Handler
"""

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
from app.utils.keyboards import main_menu_keyboard
from app.utils.messages import WELCOME_MESSAGE
from app.database import SessionLocal
from app.models.user import User

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    
    user = update.effective_user
    chat_id = update.effective_chat.id
    
    # Get or create user
    db = SessionLocal()
    db_user = db.query(User).filter(User.user_id == user.id).first()
    
    if not db_user:
        db_user = User(
            user_id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name
        )
        db.add(db_user)
        db.commit()
    
    db.close()
    
    # Send welcome message
    await update.message.reply_text(
        WELCOME_MESSAGE.format(first_name=user.first_name),
        reply_markup=main_menu_keyboard(),
        parse_mode="HTML"
    )
