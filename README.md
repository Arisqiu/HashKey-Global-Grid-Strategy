# HashKey Global Grid Trading Bot

## Overview

This repository provides a Python-based grid trading bot designed to work with the HashKey Global exchange. The bot implements a simple grid trading strategy, which automatically places buy and sell orders at predefined price levels, making it easier to capitalize on market fluctuations within a specific price range. Telegram: @ChildrenQ

## Features

- **Automated Trading:** Automatically places buy and sell orders at different price levels within a specified range.
- **Configurable Grid Parameters:** Customize the lower and upper price bounds, the number of grid levels, and the quantity per order.
- **Continuous Monitoring:** Continuously monitors the market price and adjusts orders as needed.

## Requirements

- Python 3.x
- `requests` library

You can install the required Python package with the following command:

```bash
pip install requests
```

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/HashKey-Global-Grid-Trading-Bot.git
   cd HashKey-Global-Grid-Trading-Bot
   ```

2. **Configure API Keys:**

   Replace `YOUR_HASHKEY_API_KEY` and `YOUR_HASHKEY_SECRET_KEY` with your actual HashKey Global API credentials in the Python script:

   ```python
   hashkey_api_key = 'YOUR_HASHKEY_API_KEY'
   hashkey_secret_key = 'YOUR_HASHKEY_SECRET_KEY'
   ```

3. **Configure Trading Parameters:**

   Adjust the following parameters in the `grid_trading_strategy()` function according to your trading strategy:

   - `symbol`: The trading pair (e.g., `'BTCUSDT'`).
   - `lower_price`: The lower bound of the price range for grid orders.
   - `upper_price`: The upper bound of the price range for grid orders.
   - `grid_size`: The number of grid levels.
   - `quantity_per_order`: The quantity of the asset to buy/sell per order.

## Usage

To start the grid trading bot, run the Python script:

```bash
python grid_trading_bot.py
```

The bot will place the initial grid orders and continuously monitor the market, adjusting orders as the price fluctuates.

## How It Works

1. **Grid Setup:**
   - The script calculates the grid spacing based on the upper and lower price bounds and the number of grid levels.
   - It places buy orders at each grid level and corresponding sell orders slightly above each buy order.

2. **Monitoring:**
   - The script checks the current market price at regular intervals.
   - If the price falls to a buy level, it places a new buy order and a corresponding sell order at the next grid level.

3. **Continuous Operation:**
   - The bot operates in a continuous loop, adjusting orders according to the market price.

## Notes

- Ensure you have sufficient funds in your HashKey Global account to cover the orders.
- The bot does not include any stop-loss mechanisms. Monitor the bot and the market conditions regularly.

## Disclaimer

This bot is provided for educational purposes only. Trading cryptocurrencies carries a risk, and you should only trade with money you can afford to lose. The author is not responsible for any financial losses you may incur.

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests. Telegram: @ChildrenQ

---
