"""
    File Name   : unittests\services\profit_analyzer_solution2.py
    Author      : Darryl Fernandes
    Python Ver. : 3.5.1
    Description : Unit test script to validate the get_max_profit service method
    Source File : services\profit_analyzer_solution2.py
"""

import unittest
from services.profit_analyzer_solution2 import get_max_profit


class TestMaxProfit(unittest.TestCase):

    def test_insufficient_input(self):
        #   Insufficient input scenario:-
        #           If the stock_prices_yesterday variable is an empty list or of type None,
        #           then assert if appropriate Exceptions are raised

        #   If stock_prices_yesterday is an empty list, then check if IndexError is thrown
        stock_prices_yesterday = []
        self.assertRaises(IndexError, get_max_profit, stock_prices_yesterday)

        #   If stock_prices_yesterday is a list containing less than 2 elements, then check if IndexError is thrown
        stock_prices_yesterday = [10]
        self.assertRaises(IndexError, get_max_profit, stock_prices_yesterday)

        #   If stock_prices_yesterday is of type None, then check if TypeError is thrown
        stock_prices_yesterday = None
        self.assertRaises(TypeError, get_max_profit, stock_prices_yesterday)

    def test_sufficient_input(self):
        #   Sufficient input scenario:-
        #           If the stock_prices_yesterday variable is a list containing atleast 2 or more elements
        #           Assumption: All elements provided are of type int only

        # There is opportunity to gain profit
        stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
        self.assertEqual(get_max_profit(stock_prices_yesterday), 6,
                         "Max. Profit should be equal to 6")

        # There is no opportunity to gain profit with only 2 stock prices, so minimize the loss
        stock_prices_yesterday = [10, 7]
        self.assertEqual(get_max_profit(stock_prices_yesterday), -3,
                         "Max. Profit (to minimize the loss) should be equal to -3")

        # There is no opportunity to gain profit, so minimize the loss
        stock_prices_yesterday = [10, 8, 4, 1]
        self.assertEqual(get_max_profit(stock_prices_yesterday), -2,
                         "Max. Profit (to minimize the loss) should be equal to -2")

        # There is an opportunity to gain profit, so minimize the loss
        stock_prices_yesterday = [10, 8, 7, 3, 7]
        self.assertEqual(get_max_profit(stock_prices_yesterday), 4,
                         "Max. Profit (to minimize the loss) should be equal to 4")

        # There is no opportunity to gain profit due to stagnant prices from opening to closing price
        stock_prices_yesterday = [7, 7, 7, 7, 7, 7, 7, 7]
        self.assertEqual(get_max_profit(stock_prices_yesterday), 0,
                         "Max. Profit should be equal to 0")

        # There is no opportunity to gain profit due to stagnant prices after the opening price,
        # but the minimum loss will be 0
        stock_prices_yesterday = [10, 7, 7, 7]
        self.assertEqual(get_max_profit(stock_prices_yesterday), 0,
                         "Max. Profit should be equal to 0")

        # There is opportunity to gain profit (both the min buy price and max sale price are in float)
        stock_prices_yesterday = [10, 7.54, 7.53, 7.55]
        self.assertEqual(get_max_profit(stock_prices_yesterday), 0.02,
                         "Max. Profit should be equal to 0.02")

        # There is opportunity to gain profit (min buy price is int and max sale price in float)
        stock_prices_yesterday = [10, 7.54, 7, 7.55]
        self.assertEqual(get_max_profit(stock_prices_yesterday), 0.55,
                         "Max. Profit should be equal to 0.02")

        # There is opportunity to gain profit (min buy price is float and max sale price in int)
        stock_prices_yesterday = [10, 7.54, 7.53, 8]
        self.assertEqual(get_max_profit(stock_prices_yesterday), 0.47,
                         "Max. Profit should be equal to 0.02")

        # Stock prices provided by James after code-review
        stock_prices_yesterday = [7, 3, 6, 5, 4, 1]
        self.assertEqual(get_max_profit(stock_prices_yesterday), 3,
                         "Max. Profit should be equal to 3")


if __name__ == '__main__':
    unittest.main()
