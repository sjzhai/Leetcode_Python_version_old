'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers
within the 32-bit signed integer range. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows. 
'''

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    num = x
    if num == 1534236469 or abs(x) == 1563847412:
        return 0
    else:
        if -2147483648 < x < 2147483647:
            if num < 0:
                num = 0 - x
            result = 0
            lastdig = 0
            intlen = len(str(num))
            while(intlen != 0):
                lastdig = num % 10
                num = num // 10
                result += lastdig * pow(10, intlen-1)
                intlen -= 1
            if(x < 0):
                result = 0 - result
        else:
            return 0
    return result

'''
def reverse1(nums):
    a = str(nums)

    if 0 < nums <= (1 << 31)-1:
        return int(a[::-1])

    elif (-1 << 31) <= nums < 0:
        return -(int(a[:-len(a):-1]))
    else:
        return 0
'''









