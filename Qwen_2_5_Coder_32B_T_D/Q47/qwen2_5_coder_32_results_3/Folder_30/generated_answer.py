import re

def palindromes_of_specific_lengths(s):
    s = s[14:91].lower()
    p = set()
    for l in range(55, 72):
        for i in range(len(s) - l + 1):
            t = s[i:i + l]
            if re.fullmatch('[a-z]+', t) and t == t[::-1]:
                p.add(t)
    return p