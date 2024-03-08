from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.helpers import round_step_size
api_key = 'rHWmUNZ6dmxwjr6LI4K7jdwD6sHvLEq4WWcFnqH0okVJy4neS8ZC5y2oi6cbeya4'
api_secret = 'E0uByClgaoIBMXgVzLaIXXsy0ReIYQNlZIIei6MfcL1iOq6bKNeWdolvk1zQmKYe'
client = Client(api_key, api_secret)

tick_size = 1
price_tick_size = 0.00001
expected_profit_ratio = 1+0.005


balance_usdt = client.get_asset_balance(asset='USDT')
usdt_ori = float(balance_usdt['free'])
print(balance_usdt)

trades = client.get_recent_trades(symbol='DOGEUSDT',limit=1)
buy_price = float(trades[-1]['price'])*1.001
buy_quantity = round_step_size(6/buy_price,tick_size)


order = client.order_market_buy(
    symbol='DOGEUSDT',
    quantity=buy_quantity)

balance_usdt = client.get_asset_balance(asset='USDT')
usdt_now = float(balance_usdt['free'])
free = (usdt_ori-usdt_now)/(buy_quantity*0.999) #实际购买的单个的价格
print(balance_usdt)

real_quantity = round_step_size(buy_quantity*0.999,tick_size) #实际扣去手续费得到的最小币数
sell_price0 = round_step_size(buy_price*expected_profit_ratio,price_tick_size)
sell_price = round_step_size(free*expected_profit_ratio,price_tick_size)
print(buy_price,sell_price0,sell_price)

order = client.order_limit_sell(
    symbol='DOGEUSDT',
    quantity=real_quantity,
    price=str(sell_price))