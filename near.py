'''
跟踪near
'''
import time
import datetime
from utils.create_log import append_purchase_log
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.helpers import round_step_size
from utils.fn import sum_of_negative_numbers
api_key = 'rHWmUNZ6dmxwjr6LI4K7jdwD6sHvLEq4WWcFnqH0okVJy4neS8ZC5y2oi6cbeya4'
api_secret = 'E0uByClgaoIBMXgVzLaIXXsy0ReIYQNlZIIei6MfcL1iOq6bKNeWdolvk1zQmKYe'
client = Client(api_key, api_secret)

symbol='NEARUSDT'
tarcoin = "USDT"
tick_size = 0.1
min_num = 6 #最少买入usdt数量
price_tick_size = 0.001
expected_profit_ratio = 1+0.01
fall_goal = -0.03

log_path = './log/NEARUSDT.txt'
sleeptime = 77 #间隔88秒查询一次
while True:
    try:
        candles = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1MINUTE,
                                    limit=8)  # -1为目前的数据不稳定，-2为1分钟前的数据

        data1 = candles[-2]
        data2 = candles[-3]
        data3 = candles[-4]
        data4 = candles[-5]
        data5 = candles[-6]
        data6 = candles[-7]

        magnitude1 = (float(data1[4]) - float(data1[1])) / float(data1[1])
        magnitude2 = (float(data2[4]) - float(data2[1])) / float(data2[1])
        magnitude3 = (float(data3[4]) - float(data3[1])) / float(data3[1])
        magnitude4 = (float(data4[4]) - float(data4[1])) / float(data4[1])
        magnitude5 = (float(data5[4]) - float(data5[1])) / float(data5[1])

        # if (magnitude5 + magnitude4 + magnitude3 + magnitude2 + magnitude1) < fall_goal:
        if sum_of_negative_numbers([magnitude1,magnitude5,magnitude4,magnitude3,magnitude2]) < fall_goal:
            balance_usdt = client.get_asset_balance(asset=tarcoin)
            usdt_ori = float(balance_usdt['free'])
            # print(balance_usdt)

            trades = client.get_recent_trades(symbol=symbol, limit=1)
            buy_price = float(trades[-1]['price']) * 1.001
            buy_quantity = round_step_size(min_num / buy_price, tick_size)

            order = client.order_market_buy(
                symbol=symbol,
                quantity=buy_quantity)

            balance_usdt = client.get_asset_balance(asset=tarcoin)
            usdt_now = float(balance_usdt['free'])
            free = (usdt_ori - usdt_now) / (buy_quantity * 0.999)  # 实际购买的单个的价格
            # print(balance_usdt)

            real_quantity = round_step_size(buy_quantity * 0.999, tick_size)  # 实际扣去手续费得到的最小币数
            # sell_price0 = round_step_size(buy_price * expected_profit_ratio, price_tick_size) #通过买入价格计算的出售价格
            sell_price = round_step_size(free * expected_profit_ratio, price_tick_size)  # 通过usdt的实际减少量计算的出售价格


            order = client.order_limit_sell(
                symbol=symbol,
                quantity=real_quantity,
                price=str(sell_price))

            purchase_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(buy_price, sell_price,"---",purchase_time)
            append_purchase_log(log_path, purchase_time, buy_price, sell_price)
        # else:
        #     purchase_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #     print(purchase_time,"no buy coin")
        time.sleep(sleeptime)
    except:
        time.sleep(sleeptime)