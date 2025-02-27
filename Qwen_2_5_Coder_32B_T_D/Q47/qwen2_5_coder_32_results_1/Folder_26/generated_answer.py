import re

def palindromes_of_specific_lengths(s):
    r = set()
    s = s[24:85].lower()
    for i in range(len(s) - 20):
        for j in range(i + 21, min(i + 32, len(s) + 1)):
            p = s[i:j]
            if p == p[::-1] and re.fullmatch('[a-z]+', p):
                r.add(p)
    return r