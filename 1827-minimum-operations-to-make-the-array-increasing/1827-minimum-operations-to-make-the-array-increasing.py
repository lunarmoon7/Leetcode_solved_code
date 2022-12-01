class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        prev = 0
        for i in range(n):
            if prev < nums[i]:
                prev = nums[i]
            else:
                cnt += prev - nums[i] + 1
                prev = prev + 1
        return cnt
        
                