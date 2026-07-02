class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxVal = 0
        for i in range(1, len(prices)):
            if prices[right] < prices[left]:
                left += 1
            else:
                result = prices[right] - prices[left]
                if result > maxVal:
                    maxVal = result
            right += 1
        
        return maxVal