import re

def palindromes_of_specific_lengths(s):
    s = s[23:95].lower()
    p = set()
    for i in range(len(s)):
        for j in range(i + 17, min(i + 56, len(s) + 1)):
            a = s[i:j]
            if re.fullmatch('[a-z]+', a) and a == a[::-1]:
                p.add(a)
    return p