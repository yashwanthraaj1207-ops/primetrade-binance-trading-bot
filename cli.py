import argparse

from binance.exceptions import BinanceAPIException

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_symbol
)

from bot.logging_config import logger


try:

    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading Symbol (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order Quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Limit Price"
    )

    args = parser.parse_args()

    symbol = validate_symbol(args.symbol)
    side = validate_side(args.side)
    order_type = validate_order_type(args.type)
    quantity = validate_quantity(args.quantity)

    print("\n===== ORDER SUMMARY =====")
    print("Symbol :", symbol)
    print("Side   :", side)
    print("Type   :", order_type)
    print("Qty    :", quantity)

    if order_type == "MARKET":

        response = place_market_order(
            symbol,
            side,
            quantity
        )

    else:

        if args.price is None:
            raise ValueError(
                "Price is required for LIMIT orders"
            )

        response = place_limit_order(
            symbol,
            side,
            quantity,
            args.price
        )

    print("\n===== ORDER RESPONSE =====")

    print("Order ID:", response.get("orderId"))
    print("Status:", response.get("status"))
    print("Executed Qty:", response.get("executedQty"))

    if "avgPrice" in response:
        print("Average Price:", response.get("avgPrice"))

    print("\nORDER SUCCESSFUL")

except BinanceAPIException as e:

    logger.exception(e)

    print("\nBinance API Error")
    print(e)

except ValueError as e:

    logger.exception(e)

    print("\nValidation Error")
    print(e)

except Exception as e:

    logger.exception(e)

    print("\nUnexpected Error")
    print(e)