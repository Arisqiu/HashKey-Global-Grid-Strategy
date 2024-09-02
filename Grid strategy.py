import requests
import time
import hmac
import hashlib
import math

# HashKey API credentials and endpoint
hashkey_api_key = 'YOUR_HASHKEY_API_KEY'
hashkey_secret_key = 'YOUR_HASHKEY_SECRET_KEY'
hashkey_base_url = 'https://api.hashkey.com'

# Get HashKey spot market price
def get_hashkey_spot_price(symbol):
    endpoint = f'/api/v1/market/ticker/price?symbol={symbol}'
    url = hashkey_base_url + endpoint
    response = requests.get(url)
    return float(response.json()['price'])

# Sign request (needed for authenticated endpoints)
def sign_request(params, secret_key):
    query_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
    signature = hmac.new(secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    return signature

# Place an order on HashKey
def send_hashkey_order(symbol, side, quantity, price, order_type='LIMIT'):
    endpoint = '/api/v1/order'
    url = hashkey_base_url + endpoint
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'side': side,  # BUY or SELL
        'type': order_type,
        'price': price,
        'quantity': quantity,
        'timestamp': timestamp,
        'recvWindow': 5000,
        'apiKey': hashkey_api_key
    }
    params['sign'] = sign_request(params, hashkey_secret_key)
    response = requests.post(url, data=params)
    return response.json()

# Main grid trading strategy logic
def grid_trading_strategy():
    symbol = 'BTCUSDT'
    lower_price = 25000.0  # Lower price bound
    upper_price = 35000.0  # Upper price bound
    grid_size = 10  # Number of grid levels
    quantity_per_order = 0.001  # Quantity per grid order

    # Calculate grid spacing
    grid_spacing = (upper_price - lower_price) / grid_size

    # Place initial grid orders
    for i in range(grid_size + 1):
        price = lower_price + i * grid_spacing
        send_hashkey_order(symbol, 'BUY', quantity_per_order, price)
        send_hashkey_order(symbol, 'SELL', quantity_per_order, price + grid_spacing)

    # Monitor and manage orders
    while True:
        current_price = get_hashkey_spot_price(symbol)

        # Check if any orders need to be replaced
        for i in range(grid_size + 1):
            buy_price = lower_price + i * grid_spacing
            sell_price = buy_price + grid_spacing

            if current_price <= buy_price:
                send_hashkey_order(symbol, 'BUY', quantity_per_order, buy_price)
                send_hashkey_order(symbol, 'SELL', quantity_per_order, sell_price)

        # Sleep before checking again
        time.sleep(60)

# Start the strategy
if name == "__main__":
    grid_trading_strategy()

