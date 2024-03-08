
class CoinTrader:
    def __init__(self, initial_balance):
        self.balance = initial_balance  # 初始余额
        self.records = []  # 交易记录列表，包含购买信息和预期盈利率
        self.selled_records = []

    def buy(self, coin, price_per_coin, quantity, expected_profit_ratio,times):
        """
        购买币的方法。
        参数:
        - coin: 币的名称
        - price_per_coin: 每个币的价格
        - quantity: 购买数量
        - expected_profit_ratio: 预期盈利率
        """
        total_cost = price_per_coin * quantity
        if total_cost <= self.balance:
            self.balance -= total_cost*1.001
            self.records.append({
                "coin": coin,
                "buy_price": price_per_coin,
                "quantity": quantity,
                "expected_profit_ratio": expected_profit_ratio,
                "buy_time": times,
                "sell_info": None  # 初始化卖出信息为None
            })
            # print(f"已购买 {quantity} 个 {coin}，单价 {price_per_coin}。当前余额：{self.balance}")
        # else:
        #     print(f"余额不足，无法购买 {coin}。当前余额：{self.balance}")

    def check_and_sell(self, current_price_info,times):
        """
        根据当前价格信息检查并决定是否卖出。
        参数:
        - current_price_info: 当前价格信息，格式为字典，如{"BTC": 11.0}
        """
        for record in list(self.records):  # 使用列表副本进行迭代
            current_price = current_price_info.get(record["coin"])
            if current_price:
                buy_price = record["buy_price"]
                profit_ratio = (current_price - buy_price) / buy_price
                if profit_ratio >= record["expected_profit_ratio"]:
                    total_sell_price = current_price * record["quantity"]
                    self.balance += total_sell_price*0.999
                    profit = total_sell_price - (buy_price * record["quantity"])
                    record["sell_info"] = {
                        "sell_price": current_price,
                        "sell_time": times,
                        "profit": profit
                    }
                    # print(f"已卖出 {record['quantity']} 个 {record['coin']}，单价 {current_price}。当前余额：{self.balance}，盈利：{profit}")
                    self.records.remove(record)  # 卖出后从记录中移除
                    self.selled_records.append(record)
    def direct_sell(self, current_price_info,times):
        """
        根据当前价格信息检查并决定是否卖出。
        参数:
        - current_price_info: 当前价格信息，格式为字典，如{"BTC": 11.0}
        """
        for record in list(self.records):  # 使用列表副本进行迭代
            current_price = current_price_info.get(record["coin"])
            if current_price:
                buy_price = record["buy_price"]
                profit_ratio = (current_price - buy_price) / buy_price
                if profit_ratio :
                    total_sell_price = current_price * record["quantity"]
                    self.balance += total_sell_price*0.999
                    profit = total_sell_price - (buy_price * record["quantity"])
                    record["sell_info"] = {
                        "sell_price": current_price,
                        "sell_time": times,
                        "profit": profit
                    }
                    # print(f"已卖出 {record['quantity']} 个 {record['coin']}，单价 {current_price}。当前余额：{self.balance}，盈利：{profit}")
                    self.records.remove(record)  # 卖出后从记录中移除
                    self.selled_records.append(record)

    def show_records(self):
        """显示交易记录的方法。"""
        if self.selled_records:
            print("交易记录：")
            for record in self.selled_records:
                sell_info = record.get("sell_info", {})
                try:
                    print(f"- {record['coin']}: 购买价格{record['buy_price']}, 数量{record['quantity']}, 预期盈利率{record['expected_profit_ratio']}, 卖出价格{sell_info.get('sell_price')}, 盈利{sell_info.get('profit')}, 耗时{int(sell_info.get('sell_time'))-int(record['buy_time'])}")
                except:
                    print(f"- {record['coin']}: 购买价格{record['buy_price']}, 数量{record['quantity']}, 预期盈利率{record['expected_profit_ratio']}")
        if self.records:
            print("购买记录：")
            for record in self.records:
                    print(f"- {record['coin']}: 购买价格{record['buy_price']}, 数量{record['quantity']}, 预期盈利率{record['expected_profit_ratio']}")

        print("余额:", self.balance)
    def get_balance(self):
        return self.balance

if __name__ == "__main__":
    # 示例使用
    trader = CoinTrader(initial_balance=1000)
    trader.buy("BTC", 10, 5, 0.01, 1)  # 购买BTC，预期盈利率为1%
    trader.buy("BTC", 8, 5, 0.5, 2)  # 购买BTC，预期盈利率为1%
    # 假设价格变动后，检查并可能卖出
    current_price_info = {"BTC": 14}  # 当前BTC的价格
    trader.check_and_sell(current_price_info, 3)
    trader.show_records()
