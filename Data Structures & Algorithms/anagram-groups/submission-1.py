class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = defaultdict(list)
        for st in strs:
            cnt = [0] * 26
            for i in st:
                cnt[ord(i) - ord('a')] += 1
            s[tuple(cnt)].append(st)
        return list(s.values())
