class Solution:
    def isValid(self, s: str) -> bool:
        chars = []
        isValid = True
        for c in s:
            if c == ")":
                if not chars or chars[-1] != "(":
                    return False
                chars.pop()
                continue
            if c == "}":
                if not chars or chars[-1] != "{":
                    return False
                chars.pop()
                continue
            if c == "]":
                if not chars or chars[-1] != "[":
                    return False
                chars.pop()
                continue
            chars.append(c)
        print(chars)
        if not chars and isValid:
            return True
        return False
