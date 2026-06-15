# 🚀 PrimeTrade Binance Futures Trading Bot

## Overview

PrimeTrade is a Python-based Binance Futures Testnet Trading Bot designed to execute Market and Limit orders through a command-line interface. The project demonstrates API integration, modular software architecture, input validation, logging, and error handling in a real-world trading environment.

Built using the Binance Futures Testnet, this project simulates cryptocurrency trading workflows without risking real funds.

---

## ✨ Features

* Market Order Execution
* Limit Order Execution
* BUY and SELL Order Support
* Binance Futures Testnet Integration
* Command-Line Interface (CLI)
* Input Validation
* Structured Logging
* Exception Handling
* Environment Variable Security
* Modular Code Architecture

---

## 🏗️ Architecture

CLI Input
↓
Validation Layer
↓
Order Processing Module
↓
Binance API Client
↓
Response Handling
↓
Logging & Monitoring

---

## 📂 Project Structure

```text
primetrade-binance-trading-bot/

├── client.py
├── orders.py
├── validators.py
├── logging_config.py
├── cli.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🛠️ Technologies Used

* Python
* Binance Futures API
* argparse
* python-dotenv
* Logging Module

---

## 🔒 Security

Sensitive credentials are managed through environment variables and are never hardcoded into the source code.

Example:

API_KEY=YOUR_API_KEY

API_SECRET=YOUR_API_SECRET

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yashwanthraaj1207-ops/primetrade-binance-trading-bot.git
```

Navigate to the project:

```bash
cd primetrade-binance-trading-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file using `.env.example`.

---

## 🚀 Usage

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

---

## 📊 Skills Demonstrated

* API Integration
* Software Architecture
* Command-Line Application Development
* Input Validation
* Error Handling
* Logging and Monitoring
* Environment Variable Management
* Python Development

---

## 🎯 Future Enhancements

* RSI-Based Trading Strategy
* Moving Average Strategy
* Backtesting Engine
* Telegram Notifications
* Performance Analytics Dashboard
* Multi-Asset Trading Support

---

## 👨‍💻 Author

S Yashwanth Raaj

B.E. Computer Science and Engineering (AI & ML)

Sri Sairam Engineering College

LinkedIn:
https://www.linkedin.com/in/yashwanthraaj1207

Portfolio:
https://my-own-portfolio-yashwanth-raaj.lovable.app/
