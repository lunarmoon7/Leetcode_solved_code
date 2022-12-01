class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        
        for i in range(1, n):
            prev = nums[i]
            nums[i] = max(nums[i - 1] + 1, nums[i])
            if prev < nums[i]:
                cnt += nums[i] - prev
        return cnt
        
                