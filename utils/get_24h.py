from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

def if_near_highprice_to_buy(tickers,pricenow,dis=1/4):
    high24 = float(tickers["highPrice"])
    low24 = float(tickers["lowPrice"])
    disall = high24 - low24
    disnow = pricenow - low24
    if disnow / disall > (1 - dis):  # 如果目前距离最高点较近，则不购买
        return False
    else:
        return True

if __name__ == "__main__":
    api_key = 'rHWmUNZ6dmxwjr6LI4K7jdwD6sHvLEq4WWcFnqH0okVJy4neS8ZC5y2oi6cbeya4'
    api_secret = 'E0uByClgaoIBMXgVzLaIXXsy0ReIYQNlZIIei6MfcL1iOq6bKNeWdolvk1zQmKYe'
    client = Client(api_key, api_secret)

    tickers = client.get_ticker(symbol="NEARUSDT")

    sym = "NEARUSDT"


