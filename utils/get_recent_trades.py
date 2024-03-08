from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
api_key = 'rHWmUNZ6dmxwjr6LI4K7jdwD6sHvLEq4WWcFnqH0okVJy4neS8ZC5y2oi6cbeya4'
api_secret = 'E0uByClgaoIBMXgVzLaIXXsy0ReIYQNlZIIei6MfcL1iOq6bKNeWdolvk1zQmKYe'
client = Client(api_key, api_secret)

trades = client.get_recent_trades(symbol='DOGEUSDT',limit=1)
buy_price = float(trades[-1]['price'])*1.001

print(trades)
print(buy_price)