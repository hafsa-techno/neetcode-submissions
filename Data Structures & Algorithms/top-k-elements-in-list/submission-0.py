class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = dict()
        for num in nums:
            if num in l:
                l[num] += 1
            else:
                l[num] = 1
        arr = []
        for i in range(k):
            max_value = max(l, key=l.get)
            del(l[max_value])
            arr.append(max_value)
        return (arr)