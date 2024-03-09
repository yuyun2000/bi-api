import traceback  # 导入traceback模块
import time
import datetime
from utils.create_log import append_purchase_log
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.helpers import round_step_size
from utils.fn import sum_of_negative_numbers,count_negative_numbers
from utils.get_24h import if_near_highprice_to_buy

api_key = 'rHWmUNZ6dmxwjr6LI4K7jdwD6sHvLEq4WWcFnqH0okVJy4neS8ZC5y2oi6cbeya4'
api_secret = 'E0uByClgaoIBMXgVzLaIXXsy0ReIYQNlZIIei6MfcL1iOq6bKNeWdolvk1zQmKYe'
client = Client(api_key, api_secret)

symbols=['SEIUSDT','JUPUSDT','PUNDIXUSDT']

tick_size = 0.1
min_num = 6 #最少买入usdt数量
price_tick_size = 0.0001
expected_profit_ratio = 1+0.013
fall_goal = -0.014

log_path = './log/01-4.txt'
sleeptime = 66/len(symbols) #间隔88秒查询一次

while True:
    for symbol in symbols:
        try:
            candles = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1MINUTE,
                                        limit=10)  # -1为目前的数据不稳定，-2为1分钟前的数据
            data0 = candles[-1]
            magnitude0 = (float(data0[4]) - float(data0[1])) / float(data0[1])

            data1 = candles[-2]
            data2 = candles[-3]
            data3 = candles[-4]
            data4 = candles[-5]
            data5 = candles[-6]
            data6 = candles[-7]
            data7 = candles[-8]
            data8 = candles[-9]

            magnitude1 = (float(data1[4]) - float(data1[1])) / float(data1[1])
            magnitude2 = (float(data2[4]) - float(data2[1])) / float(data2[1])
            magnitude3 = (float(data3[4]) - float(data3[1])) / float(data3[1])
            magnitude4 = (float(data4[4]) - float(data4[1])) / float(data4[1])
            magnitude5 = (float(data5[4]) - float(data5[1])) / float(data5[1])
            magnitude6 = (float(data6[4]) - float(data6[1])) / float(data6[1])
            magnitude7 = (float(data7[4]) - float(data7[1])) / float(data7[1])
            magnitude8 = (float(data8[4]) - float(data8[1])) / float(data8[1])

            magnitude = [magnitude1, magnitude5, magnitude4, magnitude3, magnitude2]
            magnitude_long = [magnitude1, magnitude5, magnitude4, magnitude3, magnitude2,magnitude8,magnitude7,magnitude6]
            if sum_of_negative_numbers(magnitude) < fall_goal and count_negative_numbers(magnitude_long) !=8 and magnitude0 >fall_goal*0.5:#连续跌五次不买；五分钟跌幅较大，而且最新一分钟还在跌的不买
                balance_usdt = client.get_asset_balance(asset="USDT")
                usdt_ori = float(balance_usdt['free'])

                trades = client.get_recent_trades(symbol=symbol, limit=1)
                buy_price = float(trades[-1]['price']) * 1.001
                buy_quantity = round_step_size(min_num / buy_price, tick_size)

                ifbuy = if_near_highprice_to_buy(client.get_ticker(symbol=symbol), buy_price,dis=1/8)
                if not ifbuy:
                    continue

                order = client.order_market_buy(
                    symbol=symbol,
                    quantity=buy_quantity)

                balance_usdt = client.get_asset_balance(asset="USDT")
                usdt_now = float(balance_usdt['free'])
                free = (usdt_ori - usdt_now) / (buy_quantity * 0.999)  # 实际购买的单个的价格

                real_quantity = round_step_size(buy_quantity * 0.999, tick_size)  # 实际扣去手续费得到的最小币数
                sell_price = round_step_size(free * expected_profit_ratio, price_tick_size)  # 通过usdt的实际减少量计算的出售价格
                if sell_price == 0:
                    sell_price = round_step_size(buy_price * expected_profit_ratio, price_tick_size)  # 通过买入价格计算的出售价格
                sell_price =  "{:.8f}".format(sell_price)
                print(symbol,"sell",real_quantity,str(sell_price))

                order = client.order_limit_sell(
                    symbol=symbol,
                    quantity=real_quantity,
                    price=str(sell_price))

                purchase_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(symbol, "---",purchase_time, "---",buy_price,sell_price)
                append_purchase_log(log_path,symbol,purchase_time, buy_price, sell_price)
            time.sleep(sleeptime)
        except:
            print('error')
            traceback.print_exc()  # 打印详细的错误信息
            # break
            time.sleep(sleeptime)
