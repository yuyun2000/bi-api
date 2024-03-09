from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
api_key = 'rHWmUNZ6dmxwjr6LI4K7jdwD6sHvLEq4WWcFnqH0okVJy4neS8ZC5y2oi6cbeya4'
api_secret = 'E0uByClgaoIBMXgVzLaIXXsy0ReIYQNlZIIei6MfcL1iOq6bKNeWdolvk1zQmKYe'
client = Client(api_key, api_secret)

# sym = "DOGEUSDT"
# sym = "ARKMUSDT"
# sym = "FTMUSDT"
# sym = "NEARUSDT"
# sym = "WLDUSDT"
sym = "ETHUSDT"

klines = client.get_historical_klines(sym, Client.KLINE_INTERVAL_1MINUTE, "7 Mar, 2024", "10 Mar, 2024")

# print(klines)




import csv
csvfile = '../data/%s-37.csv'%sym

with open(csvfile, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in klines:
        writer.writerow(row)