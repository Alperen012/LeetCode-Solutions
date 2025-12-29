class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for i in prices[1:]:
            profit = i - minPrice

            maxProfit = max(maxProfit, profit)

            minPrice = min(i, minPrice)
        
        return maxProfit
        
        