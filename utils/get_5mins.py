from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
api_key = 'rHWmUNZ6dmxwjr6LI4K7jdwD6sHvLEq4WWcFnqH0okVJy4neS8ZC5y2oi6cbeya4'
api_secret = 'E0uByClgaoIBMXgVzLaIXXsy0ReIYQNlZIIei6MfcL1iOq6bKNeWdolvk1zQmKYe'
client = Client(api_key, api_secret)


# klines = client.get_historical_klines("DOGEUSDT", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

candles = client.get_klines(symbol='DOGEUSDT', interval=Client.KLINE_INTERVAL_1MINUTE) #会获取500个，-1为目前的数据不稳定，-2为1分钟前的数据
print(candles)

data1 = candles[-2]
data2 = candles[-3]
data3 = candles[-4]
data4 = candles[-5]
data5 = candles[-6]