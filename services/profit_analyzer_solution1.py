"""
    File Name   : services\profit_analyzer_solution1.py
    Author      : Darryl Fernandes
    Python Ver. : 3.5.1
    Description : Script to identify the maximum profit that could have been gained during the previous trading day
    Unit Test   : unittests\services\profit_analyzer_solution1.py
"""


def get_max_profit(stock_prices_yesterday):
    # Identify max profit from list of stock prices as of previous day's trading session

    # If stock_prices_yesterday is of type None, then raise TypeError
    if stock_prices_yesterday is None:
        raise TypeError('Stock Prices from yesterday should be of list type')

    # If stock_prices_yesterday is an empty list or contains less than 2 elements, then raise IndexError
    if type(stock_prices_yesterday) == list and (not stock_prices_yesterday or len(stock_prices_yesterday) < 2):
        raise IndexError('Stock Prices from yesterday should have at least 2 values or more')

    max_profit = 0
    buy_at_min_value = min(stock_prices_yesterday)
    post_buy_stock_prices = stock_prices_yesterday[stock_prices_yesterday.index(buy_at_min_value)+1:]
    max_profit = max(post_buy_stock_prices) - buy_at_min_value if post_buy_stock_prices else max_profit
    return round(max_profit, 3)

