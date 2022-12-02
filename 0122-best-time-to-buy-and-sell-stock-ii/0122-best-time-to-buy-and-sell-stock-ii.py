class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit
        
        
        
        
        
        
        #         prev = prices[0]
#         top = prices[0]
#         total = 0
        
#         for i in range(prices):
#             if top > prices[i]:
                
#             if prev <= prices[i]:
#                 top = prices[i]
        
                
                