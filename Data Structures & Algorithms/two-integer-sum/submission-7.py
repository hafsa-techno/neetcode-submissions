class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = dict()
        for i, num in enumerate(nums):
            result = target - num
            print(result, i)
            if result in l:
                return ([l[result], i])
            l[num] = i

