'''
读取一个csv模拟收益
'''
from agent import CoinTrader
import numpy as np
import pandas as pd


csv_file = '../data/doge-35-39.csv'

column_names = ['timestamp', 'open', 'high', 'low', 'close']
df = pd.read_csv(csv_file, names=column_names, usecols=[0, 1, 2, 3, 4])

# 将时间戳列转换为 datetime 类型
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
# 计算每分钟的涨跌情况，收盘价高于开盘价为True，否则为False
df['is_rise'] = df['close'] > df['open']
# 计算幅度
df['magnitude'] = (df['close'] - df['open']) / df['open']

agentx = CoinTrader(80)
coin = 'test'
buy_price = 6 #单次最少买入价格

expected_profit_ratio=0.01
for idx,x in enumerate(df['magnitude']):
    if idx<5:
        continue
    fall_goal = -0.04
    if (x+df['magnitude'][idx-1]+df['magnitude'][idx-2]+df['magnitude'][idx-3]+df['magnitude'][idx-4])<fall_goal:
    # if x < -0.01 and df['magnitude'][idx-1] < - 0.01 and df['magnitude'][idx-2] < - 0.01:
        agentx.buy(coin,df['close'].iloc[idx],buy_price/df['close'].iloc[idx],expected_profit_ratio,idx)
    agentx.check_and_sell({coin:df['close'].iloc[idx]},idx)

agentx.direct_sell({coin:df['close'].iloc[idx]},idx)
agentx.show_records()
