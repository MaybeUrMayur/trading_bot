import os
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv
from bot.logging_config import logger

# Load environment variables from .env file
load_dotenv()

def get_testnet_client() -> Client:
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        logger.error("API credentials not found in environment variables.")
        raise ValueError("Please set BINANCE_API_KEY and BINANCE_API_SECRET in your .env file")
        
    try:
        # Initialize client with testnet=True for Futures testnet
        client = Client(api_key, api_secret, testnet=True)
        # Note: python-binance `testnet=True` defaults to spot testnet in older versions or might need URL tweaking for futures.
        # But for USDT-M Futures on Testnet, python-binance has a testnet option that correctly configures `testnet=True` for futures if using futures endpoints.
        # It's better to explicitly set the API URL for futures testnet to be safe, but python-binance's futures endpoints handle testnet=True flag internally.
        logger.debug("Initialized Binance Client for Testnet.")
        return client
    except Exception as e:
        logger.error(f"Failed to initialize Binance client: {e}")
        raise
