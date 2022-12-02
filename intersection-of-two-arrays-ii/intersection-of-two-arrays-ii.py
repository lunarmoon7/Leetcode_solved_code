class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
        
        # len(nums1) < len(nums2)
        c = Counter(nums1)
        ans = []
        
        for num in nums2:
            if c[num] > 0:
                ans.append(num)
                c[num] -= 1
        return ans
        