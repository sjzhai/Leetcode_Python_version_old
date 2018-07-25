
def isValid(s):
    dict_p = {'(' : ')', '{' : '}', '[' : ']'}
    # p = s
    # if p:
    #     if len(p) % 2 == 0:
    #         n = 0
    #         while(len(p) != 0):
    #             p = p.replace(' ', '')
    #             if p[n] not in dict_p:
    #                 return False
    #             if dict_p[p[n]] == p[n+1]:
    #                 p = p.replace(p[n], " ")
    #                 p = p.replace(p[n+1], " ")
    #                 p = p.strip()
    #                 n = 0
    #             elif dict_p[p[n]] != p[n+1]:
    #                 return False
    #             else:
    #                 n += 1
    #                 if len(p) <= 2:
    #                     return False
    #                 else:
    #                     pass
    #         return True
    #     else:
    #         return False
    # else:
    #     return False
    stack = []
    if (len(s) != 0) or (len(s) % 2 == 0):
        for i in range(len(s)):
            for v in dict_p.values():
                if s[0] == v:
                    return False
                elif s[i] in dict_p.keys():
                    stack.append(s[i])
                elif len(stack) == 0 or s[i] != dict_p[stack.pop()]:
                    return False
        return len(stack) == 0
    else:
        return False



if __name__ == '__main__':
    par = '{[]}'
    re = isValid(par)
    print(re)
