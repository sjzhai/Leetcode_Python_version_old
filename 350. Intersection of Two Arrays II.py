'''
350. Intersection of Two Arrays II

 Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

'''
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        li = []
        n1 = 0
        n2 = 0
        while (n1 < len(nums1) and n2 < len(nums2)):
            if nums1[n1] < nums2[n2]:
                n1 +=1
            elif nums1[n1] > nums2[n2]:
                n2 += 1
            else:
                li.append(nums1[n1])
                n1 += 1
                n2 += 1
        return li
        # for e in li:
        #     if e in [54,21,73,84,60,18,62,59,89,89,41,55,27,65,94,61,12,76,35,48,0,60,84,9,28,55,4,67,86,33]:
        #         print("Y")
        #     else:
        #         print("F")
        # return li
sol = Solution()
nums1 = [3, 1, 2]
nums2 = [1, 3]
print(sol.intersect(nums1, nums2))
##[54,21,73,84,60,18,62,59,89,89,41,55,27,65,94,61,12,76,35,48,0,60,84,9,28,55,4,67,86,33]
