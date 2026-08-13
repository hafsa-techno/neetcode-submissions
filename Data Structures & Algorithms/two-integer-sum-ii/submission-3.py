class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, value in enumerate(numbers):
            result = target - value
            if result in d and result <= value:
                print(d[result] + 1, i + 1)
                return [d[result] + 1, i + 1]
            d[value] = i
        return []