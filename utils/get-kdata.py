from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
api_key = 'rHWmUNZ6dmxwjr6LI4K7jdwD6sHvLEq4WWcFnqH0okVJy4neS8ZC5y2oi6cbeya4'
api_secret = 'E0uByClgaoIBMXgVzLaIXXsy0ReIYQNlZIIei6MfcL1iOq6bKNeWdolvk1zQmKYe'
client = Client(api_key, api_secret)

klines = client.get_historical_klines("DOGEUSDT", Client.KLINE_INTERVAL_1MINUTE, "5 Mar, 2024", "9 Mar, 2024")

# print(klines)




import csv
csvfile = '../data/doge-35-39.csv'

with open(csvfile, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in klines:
        writer.writerow(row)