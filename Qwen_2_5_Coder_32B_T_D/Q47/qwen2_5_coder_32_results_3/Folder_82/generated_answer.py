import re

def palindromes_of_specific_lengths(s):
    p = set()
    s = s[3:301].lower()
    for l in range(30, 301):
        for i in range(len(s) - l + 1):
            subs = s[i:i + l]
            if subs == subs[::-1] and re.fullmatch('[a-z]+', subs):
                p.add(subs)
    return p