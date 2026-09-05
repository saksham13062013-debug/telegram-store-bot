"""
Products Handler
"""

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from app.database import SessionLocal
from app.models.product import Product
from app.config import PRODUCTS_PER_PAGE, CURRENCY

async def products_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /products command"""
    
    db = SessionLocal()
    page = context.args[0] if context.args else 1
    
    try:
        page = int(page)
    except (IndexError, ValueError):
        page = 1
    
    # Get products
    offset = (page - 1) * PRODUCTS_PER_PAGE
    products = db.query(Product).filter(
        Product.is_active == 1
    ).limit(PRODUCTS_PER_PAGE).offset(offset).all()
    
    total = db.query(Product).filter(Product.is_active == 1).count()
    
    if not products:
        await update.message.reply_text("❌ No products available at the moment.")
        db.close()
        return
    
    # Format products message
    products_text = "🛍️ <b>Available Products:</b>\n\n"
    
    for idx, product in enumerate(products, 1):
        products_text += f"{idx}. <b>{product.name}</b>\n"
        products_text += f"   💰 {CURRENCY}{product.price}\n"
        products_text += f"   📦 Stock: {product.stock}\n\n"
    
    # Create buttons
    buttons = []
    for product in products:
        buttons.append([
            InlineKeyboardButton(
                f"Add {product.name} to Cart",
                callback_data=f"add_to_cart_{product.id}"
            )
        ])
    
    # Pagination buttons
    nav_buttons = []
    if page > 1:
        nav_buttons.append(InlineKeyboardButton("◀️ Previous", callback_data=f"products_page_{page-1}"))
    if len(products) == PRODUCTS_PER_PAGE:
        nav_buttons.append(InlineKeyboardButton("Next ▶️", callback_data=f"products_page_{page+1}"))
    
    if nav_buttons:
        buttons.append(nav_buttons)
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.message.reply_text(
        products_text,
        reply_markup=reply_markup,
        parse_mode="HTML"
    )
    
    db.close()
