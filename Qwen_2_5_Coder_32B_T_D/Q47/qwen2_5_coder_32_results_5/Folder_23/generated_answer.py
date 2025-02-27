import re

def palindromes_of_specific_lengths(s):
    s = s[23:95].lower()
    p = set()
    for i in range(len(s)):
        for j in range(i + 17, min(i + 56, len(s) + 1)):
            w = s[i:j]
            if w == w[::-1] and re.fullmatch('[a-z]+', w):
                p.add(w)
    return p