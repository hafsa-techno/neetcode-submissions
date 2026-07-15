class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            r = "".join(sorted(s))
            if r in d:
                d[r].append(s)
            else:
                d[r] = [s]
        return list(d.values())
