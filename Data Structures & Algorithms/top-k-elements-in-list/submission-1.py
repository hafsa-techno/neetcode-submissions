class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        a = []
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for i in range(k):
            max_key = max(d, key=d.get)
            d.pop(max_key)
            a.append(max_key)
        print(d)
        return a
