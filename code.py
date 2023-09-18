def isPalindrome(s: str) -> bool:
    d = ""
    a = -1
    while a >= (-1 * (len(s))):
        d += s[a]
        a -= 1
    if d.lower().replace(" ", "") == (s[0: ]).lower().replace(" ", ""):
        return True
    else:
        return False


print(isPalindrome("race car"))

# s = "string"
# d = ""
# a = -1
# while a >= (-1 *(len(s))):
#     d += s[a]
#     a -= 1
# print(d)