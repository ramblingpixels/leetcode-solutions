class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        lowest_price = prices[0]
        max_val = 0
        for i in range(1, n):
            max_val = max(max_val, prices[i] - lowest_price)
            lowest_price = min(lowest_price, prices[i])

        
        return max_val