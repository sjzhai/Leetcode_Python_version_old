'''
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
##bucket sort
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d_s = {i:0 for i in s}
        d_t = {i:0 for i in t}
        for i in s:
            if i in d_s.keys():
                d_s[i] += 1

        for i in t:
            if i in d_t.keys():
                d_t[i] += 1
        return d_s == d_t
sol = Solution()
s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))
