import os
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv
from bot.logging_config import logger

# Env
load_dotenv()

def get_testnet_client() -> Client:
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        logger.error("API credentials not found in environment variables.")
        raise ValueError("Please set BINANCE_API_KEY and BINANCE_API_SECRET in your .env file")
        
    try:
        # Client
        client = Client(api_key, api_secret, testnet=True)
        # URL
        client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        return client
    except Exception as e:
        logger.error(f"Failed to initialize Binance client: {e}")
        raise
