class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        print(prices[left])
        for i in range(len(prices) - 1):
            if prices[right] > prices[left]:
                profit += prices[right] - prices[left]
            left += 1
            right += 1
        print(profit)
        return profit