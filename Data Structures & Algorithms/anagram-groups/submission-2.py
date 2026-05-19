class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = dict()
        for i, item in enumerate(strs):
            item_sorted = ''.join(sorted(item))
            if (item_sorted in dictionary):
                continue
            dictionary[item_sorted] = []
            for s in strs:
                s2 = ''.join(sorted(s))
                if (s2 == item_sorted):
                    dictionary[item_sorted].append(s)
        return list(dictionary.values())