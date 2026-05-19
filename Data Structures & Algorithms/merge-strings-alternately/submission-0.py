class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = [] 
        first_p = 0 
        second_p = 0
        while first_p < len(word1) or second_p < len(word2):
            if first_p < len(word1):
                s.append(word1[first_p]) 
                first_p += 1
            if second_p < len(word2):
                s.append(word2[second_p])
                second_p += 1
        return ''.join(s)

# def mergeAlternately(self, word1: str, word2: str) -> str:
    # s = [''] * (len(word1) + len(word2))
    # first_p = 0
    # second_p = 0
    # i = 0
    # while first_p < len(word1) or second_p < len(word2):
        # if first_p < len(word1):
            # s[i] = word1[first_p]
            # i += 1
        # if second_p < len(word2):
            # s[i] = word2[second_p]
        # first_p += 1
        # second_p += 1
        # i += 1
    # return ''.join(s)
            
