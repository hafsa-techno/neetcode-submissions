class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = dict()
        for i, item in enumerate(strs):
            item_sorted = ''.join(sorted(item))
            print(item_sorted)
            if (item_sorted in dictionary):
                continue
            dictionary[item_sorted] = []
            dictionary[item_sorted].append(item)
            for j in range(i + 1, len(strs)):
                s2 = ''.join(sorted(strs[j]))
                if (s2 == item_sorted):
                    dictionary[item_sorted].append(strs[j])
        return list(dictionary.values())