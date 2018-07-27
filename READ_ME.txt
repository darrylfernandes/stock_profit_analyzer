############################################################################################################################

NOTES:-
1) Used TDD based approach to solve the challenge.

2.1) Used GIT for version control of local repository "\stock_profit_analyzer".
2.2) Used PyCharm IDE for development, debug and execution.
2.3) Used Python v3.5.1 for code execution

3) The Unit tests are created under "\stock_profit_analyzer\unittests\services" package
4) The Script which will get the Max Profit is under "\stock_profit_analyzer\services" package

5) The question didn't state clearly whether a buy-sell transaction was mandatory to calculate max profit.
    Hence I came up with two solutions

    Solution 1: Solution 1 is based on the Assumption that it is not necessary to buy-sell 1 stock if the input data
                does not provide an opportunity to do so

             Eg: If stock_prices_yesterday = [10, 7, 7, 7],
                 then I assumed that even if I buy 1 stock at $7, there is no leverage from subsequent stock prices
                 hence it was futile to buy-sell and hence my Max. Profit is calculated as $0 (zero)

    Solution 2:  Solution 2 is based on the Assumption that if it was mandatory to assume a buy-sell on that given day(yesterday),
                 then my aim was to check the combination of buy-sell that could have maximized my profit OR minimized the loss

             Eg: If stock_prices_yesterday = [10, 8, 4, 1],
                 then I assumed that even if I buy stock at $10, since there is no leverage from subsequent stock prices
                 hence to minimize the loss, it would be to sell at $8, since the Minimum loss would only by -$2.


    Given the best opportunity, i.e if stock_prices_yesterday = [10, 7, 5, 8, 11, 9], the max profit will be calculated
    as $6 by both the solutions that i have implemented.

6) Solution 1 :
        Script      : "\stock_profit_analyzer\services\profit_analyzer_solution1.py"
        Unit Test   : "\stock_profit_analyzer\unittests\services\profit_analyzer_solution1.py"

7) Solution 2 :
        Script      : "\stock_profit_analyzer\services\profit_analyzer_solution2.py"
        Unit Test   : "\stock_profit_analyzer\unittests\services\profit_analyzer_solution2.py"

8) Taken care of performance and also noted the overall time taken by the get_max_profit method in both the solutions.

9) Since the unit test contains all the scenarios and also appropriate calls to the get_max_profit method, I would prefer
you to run the Unit test cases (a first step process to do my code-review)



############################################################################################################################



############################################################################################################################

INSTRUCTIONS TO EXECUTE THE SCRIPT:-
-----------------------------------------


1) To Execute Solution 1, execute the Unit test in the path shown below
        Unit Test   : "\stock_profit_analyzer\unittests\services\profit_analyzer_solution1.py"

2) To Execute Solution 2, execute the Unit test in the path shown below
        Unit Test   : "\stock_profit_analyzer\unittests\services\profit_analyzer_solution2.py"


############################################################################################################################