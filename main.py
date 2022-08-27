from Array.BestTimeToBuyAndSellStock import maxProfit
def buy_and_sell_stocks(prices):
    result = maxProfit(prices)
    print(result)


if __name__ == '__main__':
    buy_and_sell_stocks([1, 2, 3, 4, 5, 6])

