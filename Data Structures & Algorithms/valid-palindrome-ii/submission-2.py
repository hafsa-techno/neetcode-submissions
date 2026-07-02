class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].lower() != s[right].lower():
                count += 1
                if count > 1:
                    return False
                if s[left] == s[right - 1]:
                    right -= 1
                    continue
                elif s[right] == s[left + 1]:
                    left += 1
                    continue
            left += 1
            right -= 1
        return True