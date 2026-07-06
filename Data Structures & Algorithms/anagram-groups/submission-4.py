class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = dict()
        for s in strs:
            s1 = "".join(sorted(s))
            if s1 in l:
                l[s1].append(s)
            else:
                l[s1] = [s]
        return list(l.values())