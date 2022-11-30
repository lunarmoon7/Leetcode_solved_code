class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        step = 0
        for i in range(n):
            if step < i:
                break
            step = max(step, i + nums[i])
            if step >= n - 1:
                return True
        return False