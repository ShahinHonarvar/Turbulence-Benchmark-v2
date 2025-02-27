import re

def palindromes_of_specific_lengths(s):
    s = s[22:96].lower()
    r = set()
    for i in range(len(s) - 51):
        for l in range(52, 56):
            if i + l <= len(s):
                t = s[i:i + l]
                if t == t[::-1] and re.fullmatch('[a-z]+', t):
                    r.add(t)
    return r