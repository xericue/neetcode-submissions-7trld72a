class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        new_max = 0
        right = 1

        while right < len(prices): # try not to mess with for loop iterations
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                new_max = max(new_max, profit)
            else:
                left = right
            right += 1

        return new_max