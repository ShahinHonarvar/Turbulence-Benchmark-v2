import re

def palindromes_of_specific_lengths(s):
    s = s[26:85].lower()
    p = set()
    for l in range(30, 47):
        for i in range(len(s) - l + 1):
            w = s[i:i + l]
            if w == w[::-1] and re.fullmatch('[a-z]+', w):
                p.add(w)
    return p