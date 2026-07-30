class Solution:
    def isValid(self, s: str) -> bool:
        d={'{':'}','(':')','[':']'};
        stac=[]
        for c1 in s:
            if stac and stac[-1] in d:
                if d[stac[-1]] == c1:
                    stac.pop()
                    continue
            stac.append(c1)
        if stac:
            return False
        return True