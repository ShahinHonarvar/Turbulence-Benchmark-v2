import re

def palindromes_of_specific_lengths(s):
    s = s[106:281].lower()
    p = set()
    for i in range(136, 152):
        for j in range(len(s) - i + 1):
            t = s[j:i + j]
            if re.match('^[a-z]+$', t) and t == t[::-1]:
                p.add(t)
    return p