"""
Bot Trading - Entry Point
Trading Bot untuk Cryptocurrency dan Saham
"""

import argparse
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class TradingBot:
    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = config_path
        self.is_running = False
        logger.info("Trading Bot initialized")
    
    def start(self, strategy: str = "rsi", dry_run: bool = True):
        """Start the trading bot"""
        self.is_running = True
        mode = "DRY RUN (No real trades)" if dry_run else "LIVE TRADING"
        logger.info(f"Starting bot in {mode} mode with {strategy} strategy")
        
        try:
            while self.is_running:
                # Main trading loop
                self.check_signals()
                self.execute_trades()
                self.update_positions()
                
        except KeyboardInterrupt:
            logger.info("Bot stopped by user")
            self.stop()
    
    def check_signals(self):
        """Check for trading signals"""
        logger.debug("Checking trading signals...")
        # TODO: Implement signal checking
    
    def execute_trades(self):
        """Execute trades based on signals"""
        logger.debug("Executing trades...")
        # TODO: Implement trade execution
    
    def update_positions(self):
        """Update and monitor open positions"""
        logger.debug("Updating positions...")
        # TODO: Implement position tracking
    
    def stop(self):
        """Stop the bot"""
        self.is_running = False
        logger.info("Bot stopped")


def main():
    parser = argparse.ArgumentParser(description="Trading Bot")
    parser.add_argument("--config", "-c", default="config.yaml", help="Config file path")
    parser.add_argument("--strategy", "-s", default="rsi", 
                       choices=["rsi", "macd", "grid", "dca"],
                       help="Trading strategy")
    parser.add_argument("--live", action="store_true", 
                       help="Run in live mode (default is dry-run)")
    parser.add_argument("--symbol", default="BTC/USDT", help="Trading pair")
    
    args = parser.parse_args()
    
    bot = TradingBot(config_path=args.config)
    
    if args.live:
        logger.warning("⚠️ LIVE TRADING MODE - Real money will be used!")
        confirm = input("Type 'YES' to confirm: ")
        if confirm != "YES":
            logger.info("Aborted live trading")
            return
    
    bot.start(strategy=args.strategy, dry_run=not args.live)


if __name__ == "__main__":
    main()
