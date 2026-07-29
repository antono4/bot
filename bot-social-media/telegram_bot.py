"""
Telegram Bot - Auto reply, commands, dan group management
"""

import os
import logging
from typing import Dict, Callable
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    filters, ContextTypes, ConversationHandler
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TelegramBot:
    def __init__(self, token: str):
        self.token = token
        self.app = Application.builder().token(token).build()
        self.handlers_registered = False
        
        # State for conversation
        self.AWAITING_INPUT = 1
        
        logger.info("Telegram Bot initialized")
    
    def register_handlers(self):
        """Register command and message handlers"""
        # Commands
        self.app.add_handler(CommandHandler("start", self.cmd_start))
        self.app.add_handler(CommandHandler("help", self.cmd_help))
        self.app.add_handler(CommandHandler("ping", self.cmd_ping))
        self.app.add_handler(CommandHandler("info", self.cmd_info))
        
        # Echo handler
        self.app.add_handler(MessageHandler(
            filters.TEXT & ~filters.COMMAND, 
            self.handle_message
        ))
        
        self.handlers_registered = True
        logger.info("Handlers registered")
    
    async def cmd_start(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        welcome = """
👋 Selamat datang!

Saya adalah Telegram Bot untuk automation.

Commands:
/start - Show this welcome message
/help - Show help
/ping - Check bot status
/info - Get chat info

Ketik pesan untuk echo!
        """
        await update.message.reply_text(welcome)
    
    async def cmd_help(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_text = """
📖 Help Menu

Available Commands:
• /start - Welcome message
• /help - Show this help
• /ping - Check if bot is alive
• /info - Show chat/group info

Features:
• Auto echo messages
• Group management ready
• Custom command support
        """
        await update.message.reply_text(help_text)
    
    async def cmd_ping(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        """Handle /ping command"""
        await update.message.reply_text("🏓 Pong!")
    
    async def cmd_info(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        """Handle /info command"""
        chat = update.effective_chat
        info = f"""
📊 Chat Info

Type: {chat.type}
ID: {chat.id}
Title: {getattr(chat, 'title', 'N/A')}
Username: @{chat.username or 'N/A'}
        """
        await update.message.reply_text(info)
    
    async def handle_message(self, update: Update, ctx: ContextTypes.DEFAULT_TYPE):
        """Handle incoming messages - Echo"""
        text = update.message.text
        await update.message.reply_text(f"You said: {text}")
    
    async def send_to_channel(self, chat_id: str, message: str):
        """Send message to specific channel/group"""
        await self.app.bot.send_message(chat_id=chat_id, text=message)
    
    def run(self):
        """Start the bot"""
        if not self.handlers_registered:
            self.register_handlers()
        
        logger.info("Bot started - Press Ctrl+C to stop")
        self.app.run_polling(allowed_updates=Update.ALL_TYPES)


def main():
    from dotenv import load_dotenv
    load_dotenv()
    
    bot = TelegramBot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    bot.run()


if __name__ == "__main__":
    main()
