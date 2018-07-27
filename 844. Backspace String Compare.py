'''
844. Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.


Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".


Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.
'''
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        ###way1###
        '''Run time 70ms'''
        # S_stack = []
        # T_stack = []
        #
        # for ele in S:
        #     if ele == "#":
        #         if S_stack:
        #             S_stack = S_stack[:-1]
        #     else:
        #         S_stack.append(ele)
        #
        # for ele in T:
        #     if ele == "#":
        #         if T_stack:
        #             T_stack = T_stack[:-1]
        #     else:
        #         T_stack.append(ele)
        # return S_stack == T_stack

        ###way2###
        '''Run time 44ms'''
        bs = '#'
        bool = True
        while(bool):
            if bs in S:
                idx = S.index(bs)
                if idx == 0:
                    S = S[1:]
                else:
                    S = S[:idx-1]+S[idx+1:]
            elif bs in T:
                idx = T.index(bs)
                if idx == 0:
                    T = T[1:]
                else:
                    T = T[:idx-1]+T[idx+1:]
            else:
                bool = False
        return S == T

sol = Solution()
S = "a#c"
T = "b"
print(sol.backspaceCompare(S, T))
