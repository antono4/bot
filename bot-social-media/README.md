# 📱 Bot Media Sosial

Bot automation untuk Twitter/X, Instagram, Telegram, dan Discord.

## 🎯 Fitur

### Twitter/X Bot
- Auto post tweet berdasarkan jadwal
- Auto reply mention
- Auto follow/unfollow
- Track hashtag analytics

### Instagram Bot
- Auto post gambar
- Auto reply DM
- Hashtag management
- Story scheduling

### Telegram Bot
- Auto reply messages
- Group management
- Channel broadcasting
- Custom commands

### Discord Bot
- Auto moderation
- Welcome messages
- Role management
- Ticket system

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Edit .env dengan token Anda
nano .env

# Run specific bot
python twitter_bot.py
python telegram_bot.py
python discord_bot.py
```

## ⚠️ Penting

- Baca dan patuhi Terms of Service setiap platform
- Jangan spam - bot akan diblokir
- Gunakan rate limiting yang wajar
- Mulai dengan mode test/dry-run

## 📁 Struktur

```
bot-social-media/
├── twitter_bot.py      # Twitter automation
├── instagram_bot.py   # Instagram automation
├── telegram_bot.py    # Telegram bot
├── discord_bot.py     # Discord bot
├── .env.example       # Environment template
├── requirements.txt   # Dependencies
└── config/
    ├── scheduler.py   # Post scheduling
    └── content.py     # Content templates
```

## 🔑 Setup Credentials

### Twitter Developer Portal
1. Buat developer account
2. Create project dan app
3. Get API Key, Secret, Access Token

### Telegram Bot Father
1. Chat dengan @BotFather
2. Ketik /newbot
3. Copy token ke .env

### Discord Developer Portal
1. Buat application
2. Enable Bot
3. Copy token
4. Add to server dengan OAuth2

## 📝 License

MIT License
