class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0
        minP = prices[0]

        for index, price in enumerate(prices):
            minP = min(minP,price)
            maxP = max(maxP,price-minP)
        
        return maxP