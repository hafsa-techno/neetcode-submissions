class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s) - 1
        i = n
        while i > n / 2 :
            s[i], s[n - i] = s[n - i], s[i]
            i -= 1
        print(s)
