class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}
        for i in range(n):
            val = target - nums[i]
            if val in hashmap:
                return [i, hashmap[val]]
            hashmap[nums[i]] = i