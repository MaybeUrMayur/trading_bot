from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.logging_config import logger

def place_order(client: Client, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    try:
        logger.info(f"Preparing to place {order_type} order: {side} {quantity} {symbol}" + (f" at {price}" if price else ""))
        
        params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity
        }
        
        if order_type == 'LIMIT':
            params['timeInForce'] = 'GTC' # Good Till Canceled is required for LIMIT orders
            params['price'] = price

        # We use futures_create_order for Binance Futures
        response = client.futures_create_order(**params)
        
        logger.info(f"Order placed successfully: Order ID {response.get('orderId')}")
        logger.debug(f"Order response details: {response}")
        
        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Exception occurred: {e.status_code} - {e.message}")
        raise
    except BinanceRequestException as e:
        logger.error(f"Binance Request Exception occurred: {e}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred while placing the order: {e}")
        raise
