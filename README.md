# Binance Futures Trading Bot

## Overview

This project is a Python-based trading bot developed for Binance Futures Testnet (USDT-M).

The application allows users to place both Market and Limit orders through a command-line interface (CLI). It includes input validation, structured logging, and exception handling to ensure reliable and maintainable execution.

This project was developed as part of a Python Developer internship assessment.

---

## Features

* Place **Market Orders**
* Place **Limit Orders**
* Support both **BUY** and **SELL** operations
* Command-line interface using `argparse`
* Input validation for user inputs
* Request and response logging
* Error handling for API and runtime exceptions
* Binance Futures Testnet integration

---

## Project Structure

```text
primetrade-binance-trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Requirements

* Python 3.x
* Binance Futures Testnet Account
* Binance Testnet API Key and Secret

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd primetrade-binance-trading-bot
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root directory and add:

```env
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
API_SECRET=YOUR_BINANCE_TESTNET_SECRET_KEY
```

---

## Usage

### Place a Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Example:

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

---

### Place a Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

Example:

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Validation Rules

### Symbol

Must be a valid futures symbol ending with `USDT`.

Examples:

```text
BTCUSDT
ETHUSDT
BNBUSDT
```

### Side

Allowed values:

```text
BUY
SELL
```

### Order Type

Allowed values:

```text
MARKET
LIMIT
```

### Quantity

Must be greater than zero.

### Price

Required only when placing a LIMIT order.

---

## Logging

All API requests, responses, and errors are automatically logged.

Log file location:

```text
logs/trading.log
```

Example log entries:

```text
2026-06-08 18:25:10 - INFO - MARKET ORDER REQUEST | BTCUSDT | BUY | 0.001
2026-06-08 18:25:11 - INFO - MARKET RESPONSE | {...}

2026-06-08 18:30:10 - INFO - LIMIT ORDER REQUEST | BTCUSDT | BUY | 0.001 | 50000
2026-06-08 18:30:11 - INFO - LIMIT RESPONSE | {...}
```

---

## Error Handling

The application handles:

* Invalid order side
* Invalid order type
* Invalid quantity
* Missing limit order price
* Binance API exceptions
* Network failures
* Unexpected runtime errors

---

## Sample Output

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

✅ ORDER SUCCESSFUL
```

---

## Assumptions

* The user has an active Binance Futures Testnet account.
* Valid API credentials are available in the `.env` file.
* Orders are executed only on the Binance Futures Testnet environment.
* Internet connectivity is available during execution.

---

## Future Improvements

Potential enhancements include:

* Stop-Limit Orders
* OCO Orders
* Interactive CLI Menu
* Trading Dashboard
* Database Integration
* Trade History Tracking

---

## Author

**S. Yashwanth Raaj**

Python Developer Internship Assessment Project

Built using Python and Binance Futures Testnet.
