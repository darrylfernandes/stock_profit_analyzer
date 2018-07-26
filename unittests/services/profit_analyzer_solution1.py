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

