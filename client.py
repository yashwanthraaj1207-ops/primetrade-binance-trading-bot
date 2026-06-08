import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

if not API_KEY or not API_SECRET:
    raise Exception("API_KEY or API_SECRET missing in .env file")

try:
    client = Client(
        API_KEY,
        API_SECRET,
        testnet=True
    )

    client.futures_change_leverage(
        symbol="BTCUSDT",
        leverage=20
    )

    print("✅ Connected to Binance Futures Testnet")
    print("✅ Leverage set to 20x")

except Exception as e:
    print("❌ Connection Failed")
    print(e)
    raise