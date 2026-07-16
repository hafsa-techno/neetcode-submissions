class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s;
        print(result)
        return result
    def decode(self, s: str) -> List[str]:
        i = 0
        arr = []
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            endWord = j + length + 1
            arr.append(s[j+1 : endWord])
            i = endWord
        return arr

        