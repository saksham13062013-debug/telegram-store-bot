"""
Callback Query Handler
"""

from telegram import Update
from telegram.ext import ContextTypes

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle callback queries and text messages"""
    
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        
        data = query.data
        
        if data == "checkout":
            await query.edit_message_text(text="Processing checkout...")
        elif data == "add_money":
            await query.edit_message_text(text="Enter amount to add:")
        elif data.startswith("add_to_cart_"):
            product_id = data.split("_")[-1]
            context.user_data['cart'] = context.user_data.get('cart', {})
            context.user_data['cart'][product_id] = context.user_data['cart'].get(product_id, 0) + 1
            await query.edit_message_text(text=f"✅ Added to cart!")
        else:
            await query.edit_message_text(text=f"Option: {data}")
    
    elif update.message and update.message.text:
        # Handle text messages
        text = update.message.text
        await update.message.reply_text(f"You said: {text}")
