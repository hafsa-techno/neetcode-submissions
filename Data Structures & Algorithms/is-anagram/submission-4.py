class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tab1 = dict()
        tab2 = dict()
        for item in s:
            if item in tab1:
                tab1[item] = tab1[item] + 1
            else:
                tab1[item] = 1
        for item in t:
            if item in tab2:
                tab2[item] = tab2[item] + 1
            else:
                tab2[item] = 1
        if len(tab1) != len(tab2):
            return False
        for key, value in tab1.items():
            if key not in tab2 or tab2[key] != value:
                return False
        return True
