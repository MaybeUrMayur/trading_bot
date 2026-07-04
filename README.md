# Binance Futures Testnet Trading Bot

A simplified Python application that can place Market and Limit orders on the Binance Futures Testnet (USDT-M) via a Command Line Interface (CLI).

## Features
- Place **MARKET** and **LIMIT** orders.
- Supports **BUY** and **SELL** sides.
- Validates user input properly.
- Logs API requests, responses, and errors to `trading_bot.log`.
- Built cleanly using `python-binance` and `argparse`.

## Setup Steps

1. **Install requirements:**
   Make sure you have Python 3.x installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Keys:**
   Create a `.env` file in the root of the project with your Binance Futures Testnet credentials:
   ```env
   BINANCE_API_KEY=your_testnet_api_key
   BINANCE_API_SECRET=your_testnet_api_secret
   ```

## How to Run Examples

Run the bot as a Python module (`python -m bot.cli`) passing the necessary arguments:

**Place a MARKET BUY Order:**
```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

**Place a LIMIT SELL Order:**
```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

## Available CLI Arguments
- `--symbol`: Trading pair symbol (e.g., BTCUSDT). Required.
- `--side`: Side of the trade (BUY or SELL). Required.
- `--type`: Order type (MARKET or LIMIT). Required.
- `--quantity`: Amount to trade. Required.
- `--price`: Price for LIMIT orders. Required if type is LIMIT.

## Assumptions
- The bot relies on the Binance Futures Testnet, so real funds are not used.
- The `python-binance` package is used to handle all request signing and timestamp management securely, as it's the standard for Python Binance integration.
