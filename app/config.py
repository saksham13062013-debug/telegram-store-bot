"""
Configuration Module
"""

import os

# Load environment variables from Railway
BOT_TOKEN = os.getenv('BOT_TOKEN', '')
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found in environment variables")

ADMIN_USER_ID = os.getenv('ADMIN_USER_ID', None)
if ADMIN_USER_ID:
    ADMIN_USER_ID = int(ADMIN_USER_ID)

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///store_bot.db')

# Payment Configuration
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY', None)
PAYPAL_API_KEY = os.getenv('PAYPAL_API_KEY', None)

# Bot Configuration
BOT_NAME = "ToolOraX Store Bot"
BOT_DESCRIPTION = "Your favorite e-commerce bot on Telegram"

# Currency
CURRENCY = os.getenv('CURRENCY', '$')
CURRENCY_CODE = "USD"

# Pagination
PRODUCTS_PER_PAGE = int(os.getenv('PRODUCTS_PER_PAGE', '5'))
ORDERS_PER_PAGE = 10

# Timeouts
INACTIVITY_TIMEOUT = 3600  # 1 hour

# Features
ENABLE_PAYMENTS = True
ENABLE_WALLET = True
ENABLE_SUPPORT = True
ENABLE_ALERTS = True
