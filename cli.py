import argparse
import logging
from client import place_market_order, place_limit_order
from validators import validate_side, validate_type, validate_price


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

symbol = args.symbol
side = args.side
order_type = args.type
quantity = args.quantity
price = args.price

validate_side(side)
validate_type(order_type)
validate_price(order_type, price)

print("\nOrder Request Summary")
print("---------------------")
print("Symbol:", symbol)
print("Side:", side)
print("Type:", order_type)
print("Quantity:", quantity)
print("Price:", price)

logging.info(f"Order request: {symbol} {side} {order_type} qty={quantity} price={price}")

try:

    if order_type == "MARKET":
        response = place_market_order(symbol, side, quantity)

    elif order_type == "LIMIT":
        response = place_limit_order(symbol, side, quantity, price)

    print("\nOrder Response")
    print("---------------------")
    print("Order ID:", response["orderId"])
    print("Status:", response["status"])
    print("Executed Qty:", response["executedQty"])
    print("Avg Price:", response["avgPrice"])

    logging.info(f"Order response: {response}")

except Exception as e:
    print("Error:", e)
    logging.error(f"Error placing order: {e}")