class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            if dp[i - 1] >= n - 1:
                return True
            if dp[i - 1] < i:
                return False
            dp[i] = max(dp[i - 1], i + nums[i])
        return dp[n - 1] >= n - 1