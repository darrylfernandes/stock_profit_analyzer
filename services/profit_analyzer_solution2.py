"""
    File Name   : services\profit_analyzer_solution2.py
    Author      : Darryl Fernandes
    Python Ver. : 3.5.1
    Description : Script to identify the maximum profit that could have been gained during the previous trading day
    Unit Test   : unittests\services\profit_analyzer_solution2.py
"""

import datetime


def get_max_profit(stock_prices_yesterday):
    # Identify max profit from list of stock prices as of previous day's trading session
    start_time = datetime.datetime.now()
    # If stock_prices_yesterday is of type None, then raise TypeError
    if stock_prices_yesterday is None:
        raise TypeError('Stock Prices from yesterday should be of list type')

    # If stock_prices_yesterday is an empty list or contains less than 2 elements, then raise IndexError
    if type(stock_prices_yesterday) == list and (not stock_prices_yesterday or len(stock_prices_yesterday) < 2):
        raise IndexError('Stock Prices from yesterday should have at least 2 values or more')

    stock_opening_price = stock_prices_yesterday[0]
    remaining_stock_prices_post_opening_price = stock_prices_yesterday[1:]

    max_profit = round(max(remaining_stock_prices_post_opening_price) - stock_opening_price, 3)

    for current_index, current_stock_price in enumerate(remaining_stock_prices_post_opening_price):
        next_stock_prices = remaining_stock_prices_post_opening_price[current_index + 1:]
        if not next_stock_prices:
            break
        buy_sell_diff = round(max(next_stock_prices) - current_stock_price, 3)
        if max_profit < buy_sell_diff:
            max_profit = buy_sell_diff
    print("Overall Time taken (in seconds) by get_max_profit method: {}".format(
        (datetime.datetime.now() - start_time).total_seconds()))
    return max_profit
