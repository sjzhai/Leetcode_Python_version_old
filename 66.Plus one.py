'''
66. Plus one

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        last = digits[-1]
        if l == 1:
            if digits[0] == 9:
                return [1,0]
            else:
                digits[0] += 1
                return digits
        else:
            digit = digits[::-1]
            for i in range(l):
                if digit[i] == 9:
                    digit[i] = 0
                    if i == l-1:
                        digit += [1]
                else:
                    digit[i] += 1
                    break
        return digit[::-1]
sol = Solution()
digits = [0]
print(sol.plusOne(digits))
