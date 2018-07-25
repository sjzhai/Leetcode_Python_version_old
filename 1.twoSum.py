'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    for i in range(len(nums)):
        prep = nums[i]
        sup = target - prep
        if sup in dict:
            return [dict[sup], i]
        dict[prep] = i


def twoSum2(nums, target):
    newlist = []
    i = 1
    prep = nums[0]
    while(i < len(nums)):
        sup = target - prep
        subli = nums[i:]
        if sup in subli:
            newlist.append(nums.index(prep))
            nums[nums.index(prep)] = ' '
            newlist.append(nums.index(sup))
            return newlist
        prep = nums[i]
        i += 1










