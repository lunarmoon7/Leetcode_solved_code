class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        cur = 0
        for i in range(n):
            if cur < nums[i]:
                cur = nums[i]
            else:
                cnt += cur - nums[i] + 1
                cur += 1
        return cnt
        
                