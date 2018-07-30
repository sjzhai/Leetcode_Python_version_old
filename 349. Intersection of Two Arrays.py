'''
349. Intersection of Two Arrays

 Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:

    Each element in the result must be unique.
    The result can be in any order.
'''

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        li = []
        hash = {ele: 0 for ele in nums1}
        for k in nums2:
            if k in hash.keys() and k not in li:
                li.append(k)
        return li


sol = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(sol.intersection(nums1, nums2))
