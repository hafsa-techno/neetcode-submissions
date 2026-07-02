# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = dict()
        for i,num in enumerate(nums):
            result = target - num
            if result in di:
                return [di[result], i]
            di[num] = i


