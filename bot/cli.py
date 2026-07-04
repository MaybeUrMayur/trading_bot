import argparse
import sys
from bot.client import get_testnet_client
from bot.validators import validate_order_type, validate_side, validate_quantity, validate_price
from bot.orders import place_order
from bot.logging_config import logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", type=str, required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, help="BUY or SELL")
    parser.add_argument("--type", type=str, required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=str, required=True, help="Quantity to trade")
    parser.add_argument("--price", type=str, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        # Validation
        symbol = args.symbol.upper()
        order_type = validate_order_type(args.type)
        side = validate_side(args.side)
        quantity = validate_quantity(args.quantity)
        price = validate_price(order_type, args.price)

        # Client
        client = get_testnet_client()

        # Order
        print(f"\n--- Order Request Summary ---")
        print(f"Symbol:   {symbol}")
        print(f"Side:     {side}")
        print(f"Type:     {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price:    {price}")
        print(f"-----------------------------\n")
        
        print("Sending request to Binance Futures Testnet...")
        response = place_order(client, symbol, side, order_type, quantity, price)

        # Response
        print("\n--- Order Response ---")
        print(f"Status:       SUCCESS")
        print(f"Order ID:     {response.get('orderId')}")
        print(f"Order Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        if response.get('avgPrice'):
            print(f"Average Price:{response.get('avgPrice')}")
        print("----------------------\n")

    except ValueError as e:
        print(f"\n[Validation Error] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[Execution Error] {e}")
        print("Please check trading_bot.log for detailed information.")
        sys.exit(1)

if __name__ == "__main__":
    main()
