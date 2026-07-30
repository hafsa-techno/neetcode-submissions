class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            result = target - n
            if result in d:
                print(d[result], i)
                return [d[result], i]
            d[n] = i