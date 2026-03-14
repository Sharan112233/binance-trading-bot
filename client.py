import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")


client = Client(API_KEY, API_SECRET)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

def place_market_order(symbol, side, quantity):
    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )
    return order


def place_limit_order(symbol, side, quantity, price):
    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        timeInForce="GTC",
        quantity=quantity,
        price=price
    )
    return order