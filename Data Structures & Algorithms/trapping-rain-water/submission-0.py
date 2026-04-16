class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        n = len(height)
        prefix, suffix = [0] * n, [0] * n
        prefix[0], suffix[-1] = height[0], height[-1]
        v = 0
        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i])
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        for i in range(n):
            v += min(prefix[i], suffix[i]) - height[i]
        return v