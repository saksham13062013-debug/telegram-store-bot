"""
Orders Handler
"""

from telegram import Update
from telegram.ext import ContextTypes
from app.database import SessionLocal
from app.models.order import Order

async def orders_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /orders command"""
    
    user_id = update.effective_user.id
    db = SessionLocal()
    
    # Get user's orders
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    
    if not orders:
        await update.message.reply_text(
            "📦 <b>Your Orders</b>\n\n"
            "You haven't placed any orders yet.",
            parse_mode="HTML"
        )
        db.close()
        return
    
    # Format orders message
    orders_text = "📦 <b>Your Orders:</b>\n\n"
    
    for order in orders:
        orders_text += f"Order #{order.order_number}\n"
        orders_text += f"Status: {order.status.upper()}\n"
        orders_text += f"Total: ${order.total_price}\n"
        orders_text += f"Date: {order.created_at.strftime('%Y-%m-%d %H:%M')}\n\n"
    
    await update.message.reply_text(
        orders_text,
        parse_mode="HTML"
    )
    
    db.close()
