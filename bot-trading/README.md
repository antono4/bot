# 🤖 Bot Trading/Investasi

Bot untuk trading cryptocurrency dan saham secara otomatis.

## 📋 Fitur

- **Crypto Trading**: Binance, Coinbase, Kraken API integration
- **Stock Trading**: Yahoo Finance, Alpaca, Interactive Brokers
- **Technical Analysis**: RSI, MACD, Bollinger Bands, Moving Averages
- **Risk Management**: Stop-loss, Take-profit, Position sizing
- **Backtesting**: Test strategi dengan data historis

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Copy config
cp config.example.yaml config.yaml

# Edit config dengan API keys Anda
nano config.yaml

# Run bot
python main.py
```

## ⚠️ Disclaimer

**PERINGATAN**: Trading memiliki risiko tinggi. Bot ini hanya untuk tujuan edukasi. Selalu lakukan backtesting sebelum live trading. Modal yang hilang tidak bisa dikembalikan.

## 📁 Struktur

```
bot-trading/
├── main.py              # Entry point
├── config.example.yaml  # Contoh konfigurasi
├── requirements.txt     # Dependencies
├── strategies/          # Strategi trading
│   ├── rsi.py          # RSI Strategy
│   ├── macd.py         # MACD Strategy
│   └── grid.py         # Grid Trading
├── exchanges/           # Exchange integrations
│   ├── binance.py
│   ├── coinbase.py
│   └── alpaca.py
└── utils/
    ├── indicators.py    # Technical indicators
    └── risk.py         # Risk management
```

## 🔑 Konfigurasi API

### Binance
```yaml
binance:
  api_key: "YOUR_API_KEY"
  api_secret: "YOUR_API_SECRET"
  testnet: true  # Mulai dengan testnet!
```

### Alpaca (Stocks)
```yaml
alpaca:
  api_key: "YOUR_API_KEY"
  api_secret: "YOUR_API_SECRET"
  paper: true  # Paper trading dulu!
```

## 📊 Strategi yang Tersedia

| Strategi | Deskripsi | Risk Level |
|---------|-----------|------------|
| RSI | Beli saat oversold, jual saat overbought | Medium |
| MACD | Moving Average Crossover | Medium |
| Grid | Buy low sell high otomatis | Low |
| DCA | Dollar Cost Averaging | Very Low |

## 🧪 Backtesting

```bash
python backtest.py --strategy rsi --symbol BTC/USDT --days 365
```

## 📝 License

MIT License - Gunakan dengan risiko sendiri!
