"""
    File Name   : unittests\services\profit_analyzer_solution1.py
    Author      : Darryl Fernandes
    Python Ver. : 3.5.1
    Description : Unit test script to validate the get_max_profit service method
    Source File : services\profit_analyzer_solution1.py
"""

import unittest
from services.profit_analyzer_solution1 import get_max_profit


class TestMaxProfit(unittest.TestCase):

    def test_scenario1(self):
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

    def test_scenario2(self):
        #   Sufficient input scenario:-
        #           If the stock_prices_yesterday variable is a list containing atleast 2 or more elements
        #           Assumption: All elements provided are of type int only

        stock_prices_yesterday = [10, 7]

        self.assertEqual(get_max_profit(stock_prices_yesterday), 0,
                         "Max. Profit should be equal to 0")

        stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
        self.assertEqual(get_max_profit(stock_prices_yesterday), 6,
                         "Max. Profit should be equal to 6")


if __name__ == '__main__':
    unittest.main()


