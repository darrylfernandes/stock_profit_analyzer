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


if __name__ == '__main__':
    unittest.main()
