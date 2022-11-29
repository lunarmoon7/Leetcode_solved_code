class Solution(object):
    def minProductSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # Maximize product Sum => sort() + sort(reverse=True)
        sums, n = 0, len(nums1)
        nums1.sort()
        nums2.sort()
        
        for i in range(n):
            sums += nums1[i] * nums2[~i]
        return sums
        
        