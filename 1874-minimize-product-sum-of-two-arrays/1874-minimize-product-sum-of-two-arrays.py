class Solution(object):
    def minProductSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sums, n = 0, len(nums1)
        nums1.sort()
        nums2.sort(reverse=True)
        
        for num1, num2 in zip(nums1, nums2):
            sums += num1 * num2
        return sums
        
        