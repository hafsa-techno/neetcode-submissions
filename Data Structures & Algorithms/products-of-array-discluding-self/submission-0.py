class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        arr = []
        for i, num in enumerate(nums):
            if not left:
                left.append(num)
            else:
                left.append(left[i - 1] * num)
        print(left)
        i = len(nums) - 1
        j = 0
        while i >= 0:
            if not right:
                right.append(nums[i])
            else:
                right.append(right[j - 1] * nums[i])
            i -= 1
            j += 1
        right = right[::-1]
        print(right)
        for i,num in enumerate(nums):
            ln = 1
            rn = 1
            if i > 0:
                ln = left[i - 1]
            if i < len(nums) - 1:
                rn = right[i + 1]
            arr.append(ln * rn)
        return arr 
