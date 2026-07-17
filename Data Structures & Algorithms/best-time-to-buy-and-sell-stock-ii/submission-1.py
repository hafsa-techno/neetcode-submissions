class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        print(prices[left])
        while left < right and right < len(prices):
            if prices[right] > prices[left]:
                profit += prices[right] - prices[left]
            left += 1
            right += 1
        return profit