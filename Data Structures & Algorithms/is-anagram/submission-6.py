class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for x in list(s):
            d1[x] = d1.get(x, 0) + 1
        for x in list(t):
            d2[x] = d2.get(x, 0) + 1
        if len(d1) != len(d2):
            return False
        for key, value in d1.items():
            if key not in d2 or d2[key] != value:
                return False
        return True