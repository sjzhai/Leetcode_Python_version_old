'''
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4

'''
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ###Way1###
        # hash = {}
        # for ele in nums:
        #     if ele not in hash.keys():
        #         hash[ele] = 1
        #     else:
        #         hash[ele] += 1
        # for n in nums:
        #     if hash[n] == 1:
        #         return n

        ###Way2###
        # hash = {}
        # for ele in nums:
        #     if ele not in hash.keys():
        #         hash[ele] = 1
        #     else:
        #         hash[ele] += 1
        # idx = list(hash.values()).index(1)
        # return list(hash.keys())[idx]

        ###Way3###
        hash = collections.Counter(nums)
        return list(hash.keys())[list(hash.values()).index(1)]

sol = Solution()
nums = [4,1,2,1,2]
print(sol.singleNumber(nums))
