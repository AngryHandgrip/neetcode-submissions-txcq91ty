class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for i in strs:
            sorted_i = ''.join(sorted(i))
            if sorted_i not in list(s.keys()):
                s[sorted_i] = []
            s[sorted_i].append(i)
        return list(s.values())