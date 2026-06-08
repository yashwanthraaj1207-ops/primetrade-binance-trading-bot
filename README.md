\# Binance Futures Trading Bot



\## Overview



This project is a simple Python-based trading bot developed for the Binance Futures Testnet (USDT-M).



The bot allows users to place both Market and Limit orders through a command-line interface. It includes input validation, logging, and error handling to ensure reliable execution and easier debugging.



This project was built as part of a Python Developer application task.



\---



\## Features



\* Place \*\*Market Orders\*\*

\* Place \*\*Limit Orders\*\*

\* Support for both \*\*BUY\*\* and \*\*SELL\*\* orders

\* Command-line interface using `argparse`

\* Input validation

\* Request and response logging

\* Error handling for invalid inputs and API exceptions

\* Binance Futures Testnet integration



\---



\## Project Structure



```text

primetrade-binance-trading-bot
│
├── bot
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs
│   └── trading.log
│
├── cli.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore



\## Requirements



\* Python 3.x

\* Binance Futures Testnet Account

\* Binance Testnet API Key and Secret



\---



\## Installation



\### Clone or Download the Project



```bash

git clone <repository-url>

cd trading\_bot

```



\### Create a Virtual Environment



```bash

python -m venv venv

```



\### Activate Virtual Environment



Windows:



```bash

venv\\Scripts\\activate

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\---



\## Environment Variables



Create a `.env` file in the project root directory and add:



```env

API\_KEY=YOUR\_BINANCE\_TESTNET\_API\_KEY

API\_SECRET=YOUR\_BINANCE\_TESTNET\_SECRET\_KEY

```



\---



\## Usage



\### Place a Market Order



```bash

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

```



Example:



```bash

python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001

```



\---



\### Place a Limit Order



```bash

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000

```



Example:



```bash

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000

```



\---



\## Logging



All API requests, responses, and errors are logged automatically.



Log file location:



```text

logs/trading.log

```



The log file contains:



\* Market Order Requests

\* Market Order Responses

\* Limit Order Requests

\* Limit Order Responses

\* Validation Errors

\* API Errors



\---



\## Error Handling



The application handles:



\* Invalid order side

\* Invalid order type

\* Invalid quantity

\* Missing limit order price

\* Binance API exceptions

\* Unexpected runtime errors



\---



\## Assumptions



\* The user has an active Binance Futures Testnet account.

\* API credentials are valid and stored in the `.env` file.

\* Orders are executed only on the Binance Futures Testnet environment.

\* Internet connectivity is available while placing orders.



\---



\## Sample Output



```text

===== ORDER SUMMARY =====



Symbol : BTCUSDT

Side   : BUY

Type   : MARKET

Qty    : 0.001



===== ORDER RESPONSE =====



Order ID: 123456789

Status: FILLED

Executed Qty: 0.001



ORDER SUCCESSFUL

```



\---



\## Author



Developed as part of a Python Developer internship application task using Python and Binance Futures Testnet.



