import datetime

def append_purchase_log(file_path, purchase_time, purchase_price, sell_price):
    with open(file_path, 'a') as f:
        log_line = f"{purchase_time}, 购买价格: {purchase_price}, 卖出价格: {sell_price}\n"
        f.write(log_line)

# 调用示例
# file_path = 'purchase_log.txt'
# purchase_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# purchase_price = 100
# sell_price = 120
# append_purchase_log(file_path, purchase_time, purchase_price, sell_price)
