class Solution(object):
    def maxProfit(self, prices):

        if len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0        

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit