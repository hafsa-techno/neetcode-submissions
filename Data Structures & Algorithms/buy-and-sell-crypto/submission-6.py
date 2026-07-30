class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices):
            print(left, right, prices[right], prices[left])
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right = right + 1
        print(maxProfit)
        return maxProfit