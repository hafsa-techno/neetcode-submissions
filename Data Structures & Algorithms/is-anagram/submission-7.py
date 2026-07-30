class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        if len(s) != len(t):
            return False
        for c1 in s:
            d1[c1] = d1.get(c1, 0) + 1
        for c2 in t:
            d2[c2] = d2.get(c2, 0) + 1
        for key, value in d1.items():
            if key not in d2 or d2[key] != value:
                return False
        return True