import re

def palindromes_of_specific_lengths(s):
    s = s[34:91].lower()
    p = set()
    for i in range(len(s)):
        for j in range(14, 40):
            if i + j <= len(s):
                t = s[i:i + j]
                if re.fullmatch('[a-z]+', t) and t == t[::-1]:
                    p.add(t)
    return p