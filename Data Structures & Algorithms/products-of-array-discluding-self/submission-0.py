class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = [0] * n
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = suffix[-1] = 1
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(n):
            s[i] = prefix[i] * suffix[i]
        return s