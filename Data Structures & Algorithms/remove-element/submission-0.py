class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count: int = 0
        new_nums = []
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count