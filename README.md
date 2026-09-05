# 🤖 Telegram Store Bot

एक complete e-commerce bot जो Telegram पर काम करता है। यह bot products को show करता है, shopping cart, orders, और wallet functionality provide करता है।

## ✨ Features

- 🛍️ **Product Catalog** - सभी products को browse करें pagination के साथ
- 🛒 **Shopping Cart** - Items को cart में add करें
- 💳 **Wallet** - Wallet balance check करें और money add करें
- 📦 **Orders** - अपने सभी orders को देखें
- 💬 **Support** - Customer support के लिए
- 🔧 **Admin Panel** - Admin users के लिए (optional)

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Telegram Account
- Bot Token from [@BotFather](https://t.me/botfather)

### Installation

#### 1. Repository Clone करो
```bash
git clone https://github.com/saksham13062013-debug/telegram-store-bot.git
cd telegram-store-bot
```

#### 2. Dependencies Install करो
```bash
pip install -r requirements.txt
```

#### 3. Environment Variables Setup करो
`.env` file बनाओ:
```bash
cp .env.example .env
```

फिर अपनी values add करो:
```
BOT_TOKEN=your_bot_token
ADMIN_USER_ID=your_user_id
DATABASE_URL=sqlite:///store_bot.db
CURRENCY=$
PRODUCTS_PER_PAGE=5
```

#### 4. Database Initialize करो
```bash
python -c "from app.database import init_db; init_db()"
```

#### 5. Bot Run करो
```bash
python main.py
```

## 📱 Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Bot को शुरू करो |
| `/help` | Help देखो |
| `/products` | सभी products देखो |
| `/cart` | Shopping cart देखो |
| `/orders` | अपने orders देखो |
| `/wallet` | Wallet balance check करो |
| `/support` | Support के लिए contact करो |
| `/admin` | Admin panel (admin users only) |

## 🌐 Railway पर Deploy करना

### Step 1: GitHub पर Push करो
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### Step 2: Railway Account बनाओ
- [railway.app](https://railway.app/) खोलो
- GitHub से sign up करो

### Step 3: Deploy करो
1. Railway dashboard खोलो
2. "New Project" दबाओ
3. "Deploy from GitHub" select करो
4. अपना repository select करो

### Step 4: Environment Variables Add करो
Railway dashboard में:
1. Variables tab खोलो
2. ये variables add करो:
   - `BOT_TOKEN` - तुम्हारा bot token
   - `ADMIN_USER_ID` - तुम्हारा user ID
   - `DATABASE_URL` - PostgreSQL connection string
   - `CURRENCY` - $
   - `PRODUCTS_PER_PAGE` - 5

### Step 5: Deployment शुरू करो
Railway automatically deploy करेगा। जब हरा tick दिखे, bot online है! ✅

## 📁 Project Structure

```
telegram-store-bot/
├── main.py                 # Main entry point
├── requirements.txt        # Dependencies
├── Procfile               # Railway configuration
├── .env.example           # Environment variables example
└── app/
    ├── config.py          # Configuration
    ├── database.py        # Database setup
    ├── models/            # Database models
    │   ├── user.py
    │   ├── product.py
    │   ├── order.py
    │   └── wallet.py
    └── handlers/          # Command handlers
        ├── start.py
        ├── products.py
        ├── cart.py
        ├── orders.py
        ├── wallet.py
        ├── support.py
        ├── admin.py
        └── callbacks.py
```

## 🛠️ Development

### Local Development
```bash
# Terminal 1: Bot चलाओ
python main.py

# Terminal 2: Tests चलाओ (optional)
python -m pytest
```

### Database के साथ
Bot SQLAlchemy ORM use करता है जो different databases को support करता है:
- SQLite (development के लिए)
- PostgreSQL (production के लिए)

## 📝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### Bot Crashed हो गया?
1. Railway logs check करो
2. Environment variables verify करो
3. Database connection check करो

### Commands काम नहीं कर रहे?
1. Bot token सही है check करो
2. Bot को restart करो
3. Logs देखो

### Database Error?
1. DATABASE_URL सही है check करो
2. PostgreSQL running है check करो (अगर use कर रहे हो)

## 📞 Support

अगर कोई issue हो तो:
1. GitHub Issues खोलो
2. Error message और logs share करो
3. अपनी environment बताओ

---

**Made with ❤️ by saksham13062013**
