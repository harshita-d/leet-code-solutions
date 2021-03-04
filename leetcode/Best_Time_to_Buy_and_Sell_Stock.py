class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	""" Keep track of min element than find the profit between current element and min element
    		at last store the value of max profit.
    	"""
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
    