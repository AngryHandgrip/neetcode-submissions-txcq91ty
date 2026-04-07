class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = defaultdict(int)
        for i in nums:
            s[i] += 1
        t_s = list(sorted(s.items(), key=lambda x: x[1], reverse=True))[:k]
        return [x[0] for x in t_s]