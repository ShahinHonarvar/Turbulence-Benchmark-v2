import re

def palindromes_of_specific_lengths(s):
    s = s[125:284].lower()
    p = set()
    for i in range(len(s)):
        for l in range(109, 127):
            if i + l <= len(s):
                sub = s[i:i + l]
                if re.match('^[a-z]+$', sub) and sub == sub[::-1]:
                    p.add(sub)
    return p