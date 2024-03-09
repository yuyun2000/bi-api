'''
计算参数
'''
from agent import CoinTrader
import numpy as np
import pandas as pd
from fn import sum_of_negative_numbers

csv_file = '../data/ETHUSDT-37.csv'

column_names = ['timestamp', 'open', 'high', 'low', 'close']
df = pd.read_csv(csv_file, names=column_names, usecols=[0, 1, 2, 3, 4])

# 将时间戳列转换为 datetime 类型
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
# 计算每分钟的涨跌情况，收盘价高于开盘价为True，否则为False
df['is_rise'] = df['close'] > df['open']
# 计算幅度
df['magnitude'] = (df['close'] - df['open']) / df['open']


coin = 'test'
buy_price = 6 #单次最少买入价格

max_money = 0
goal = []

for i in [0.01,0.02,0.03,0.04,0.05]:
    expected_profit_ratio=i
    for j in [-0.005,-0.01,-0.02,-0.03,-0.04,-0.05,-0.06]:
        agentx = CoinTrader(80)
        for idx, x in enumerate(df['magnitude']):
            if idx < 5:
                continue
            fall_goal = j
            # if (x + df['magnitude'][idx - 1] + df['magnitude'][idx - 2] + df['magnitude'][idx - 3] + df['magnitude'][
                # idx - 4]) < fall_goal:
            if sum_of_negative_numbers(
                        [df['magnitude'][idx - 1], df['magnitude'][idx - 2], df['magnitude'][idx - 3],
                         df['magnitude'][idx - 4], x]) < fall_goal:
                agentx.buy(coin, df['close'].iloc[idx], buy_price / df['close'].iloc[idx], expected_profit_ratio, idx)
            agentx.check_and_sell({coin: df['close'].iloc[idx]}, idx)

        agentx.direct_sell({coin: df['close'].iloc[idx]}, idx)
        last = agentx.get_balance()
        print(last)
        if last > max_money:
            max_money = last
            goal=[i,j]
print(goal)
