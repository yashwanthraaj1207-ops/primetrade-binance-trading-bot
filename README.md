# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot developed for Binance Futures Testnet (USDT-M). The application allows users to place Market and Limit orders through a command-line interface while maintaining a clean architecture, proper validation, structured logging, and exception handling.

The project was developed as part of a Python Developer internship assessment and focuses on building a reusable and maintainable trading application.

---

## Features

### Trading Features

* Place Market Orders
* Place Limit Orders
* Support BUY and SELL operations
* Binance Futures Testnet integration

### Validation Features

* Symbol validation
* Order type validation
* Side validation
* Quantity validation
* Limit order price validation

### Engineering Features

* Modular project structure
* Command Line Interface (CLI)
* Structured logging
* Exception handling
* Environment-based configuration
* Reusable code organization

---

## Project Architecture

```text
trading_bot/
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
├── requirements.txt
├── README.md
└── .env.example
```

### Architecture Explanation

| File              | Responsibility                         |
| ----------------- | -------------------------------------- |
| cli.py            | Entry point and command-line interface |
| client.py         | Binance Futures client initialization  |
| orders.py         | Order placement logic                  |
| validators.py     | Input validation logic                 |
| logging_config.py | Logging configuration                  |
| trading.log       | Stores requests, responses, and errors |

---

## Technology Stack

* Python 3.x
* python-binance
* argparse
* python-dotenv
* logging

---

## Prerequisites

Before running the project, ensure you have:

* Python 3.x installed
* Binance Futures Testnet account
* Binance Futures Testnet API Key
* Internet connection

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd trading_bot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a file named `.env` in the project root directory.

Example:

```env
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
API_SECRET=YOUR_BINANCE_TESTNET_SECRET_KEY
```

---

## Running the Application

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Example Output:

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

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

---

## Validation Rules

### Symbol

Supported format:

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

Required only for LIMIT orders.

---

## Logging

The application records all trading activity in:

```text
logs/trading.log
```

Logged information includes:

* Market Order Requests
* Market Order Responses
* Limit Order Requests
* Limit Order Responses
* Validation Errors
* API Errors
* Unexpected Exceptions

Example:

```text
2026-06-08 18:25:10 - INFO - MARKET ORDER REQUEST | BTCUSDT | BUY | 0.001
2026-06-08 18:25:11 - INFO - MARKET RESPONSE | {...}
```

---

## Error Handling

The application handles:

### Validation Errors

Examples:

* Invalid symbol
* Invalid order type
* Invalid side
* Invalid quantity
* Missing limit price

### Binance API Errors

Examples:

* Invalid API credentials
* Insufficient balance
* Invalid trading symbol

### Runtime Errors

Examples:

* Network connectivity issues
* Unexpected exceptions

---

## Assumptions

* User possesses valid Binance Futures Testnet credentials.
* Orders are executed only on Binance Futures Testnet.
* Internet connectivity is available during execution.
* The project is intended for educational and assessment purposes only.

---

## Deliverables Included

* Source Code
* README Documentation
* requirements.txt
* Logging Output
* Market Order Example
* Limit Order Example

---

## Future Improvements

Potential enhancements include:

* Stop-Limit Orders
* OCO Orders
* Grid Trading Strategy
* Interactive CLI Menus
* Web Dashboard
* Database Integration
* Trade History Analytics

---

## Author

S. Yashwanth Raaj

Python Developer Internship Assessment Project

Built using Python and Binance Futures Testnet.
