"""
Cart Handler
"""

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def cart_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /cart command"""
    
    user_id = update.effective_user.id
    
    # Get cart from user context (store in memory for this example)
    cart = context.user_data.get('cart', {})
    
    if not cart:
        await update.message.reply_text(
            "🛒 Your cart is empty.\n\n"
            "Browse products and add items to your cart."
        )
        return
    
    # Format cart message
    cart_text = "🛒 <b>Your Shopping Cart:</b>\n\n"
    total = 0
    
    for product_id, quantity in cart.items():
        cart_text += f"Product ID: {product_id}\n"
        cart_text += f"Quantity: {quantity}\n\n"
    
    cart_text += f"<b>Total: ${total}</b>"
    
    # Create checkout button
    buttons = [
        [InlineKeyboardButton("💳 Checkout", callback_data="checkout")],
        [InlineKeyboardButton("🛍️ Continue Shopping", callback_data="products")]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.message.reply_text(
        cart_text,
        reply_markup=reply_markup,
        parse_mode="HTML"
    )
