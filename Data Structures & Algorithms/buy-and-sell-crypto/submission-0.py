class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minbuy = prices[0]
        
        for i in prices:
            maxP = max(maxP,i - minbuy)
            minbuy = min(minbuy, i)
        return maxP