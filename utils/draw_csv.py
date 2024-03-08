'''
画出csv图形
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def drwa_csv(csv_file):
    # 读取 CSV 文件，只关注前5列
    column_names = ['timestamp', 'open', 'high', 'low', 'close']
    df = pd.read_csv(csv_file, names=column_names, usecols=[0, 1, 2, 3, 4])

    # 将时间戳列转换为 datetime 类型
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # 计算每分钟的涨跌情况，收盘价高于开盘价为True，否则为False
    df['is_rise'] = df['close'] > df['open']

    # 计算幅度
    df['magnitude'] = (df['close'] - df['open']) / df['open']

    # 绘制柱状图
    plt.figure(figsize=(14, 8))

    # 遍历数据，根据涨跌情况分别绘制红绿柱子，并显示幅度
    for i in range(len(df)):
        color = 'green' if df['is_rise'].iloc[i] else 'red'
        bottom_price = min(df['open'].iloc[i], df['close'].iloc[i])
        magnitude = df['magnitude'].iloc[i]
        plt.bar(df['timestamp'].iloc[i], abs(df['close'].iloc[i] - df['open'].iloc[i]),
                bottom=bottom_price, width=0.0007, color=color)
        # 在柱子上方显示幅度，保留两位小数
        # plt.text(df['timestamp'].iloc[i], df['close'].iloc[i] + (0.0001 * max(abs(magnitude), 0.0005)),
        #          f'{magnitude:.2%}', ha='center', va='bottom', rotation=90, fontsize=8)

    # 添加图表标题和轴标签
    # plt.title('Price Changes Per Minute with Magnitude')
    # plt.xlabel('Time')
    # plt.ylabel('Price')

    # 自动调整 x 贴的日期标签，以免重叠
    plt.gcf().autofmt_xdate()

    # 显示图表
    plt.show()




drwa_csv('../data/PEPEUSDT-1m-2024-03-05.csv')
