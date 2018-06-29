
def myAtoi(str):
    s = str
    num = "0123456789"
    neg = False
    if s[0] not in num:
        if s[0] == " ":
            s = s.strip()
        elif s[0] == '-':
            neg = True
        else:
            return 0
    for e in s:
        if e not in num:
            s = s.replace(e, "")
    i = int(s)
    if neg == True:
        i = 0 - i
    if i > 0x7fffffff:
        return 0x7fffffff
    elif i < -0x80000000:
        return -0x80000000
    return i
if __name__ == '__main__':
    str = "-91283472332"
    result = myAtoi(str)
    print(result)
