class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        max_cnt = 1
        for i in nums_set:
            if (i - 1) not in nums_set:
                cnt = 1
                curr_i = i
                while (curr_i + 1) in nums_set:
                    cnt += 1
                    curr_i += 1
                max_cnt = max(max_cnt, cnt)
        return max_cnt