def lengthOfLastWord(s: str) -> int:
    s = s[::-1].lstrip()
    num = 0
    if s.__contains__(" "):
        for i in s[ :s.index(" ")]:
            num += 1
    else:
        num = len(s)
    return num

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))