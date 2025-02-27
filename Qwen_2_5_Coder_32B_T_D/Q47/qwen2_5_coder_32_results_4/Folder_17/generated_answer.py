import re

def palindromes_of_specific_lengths(s):
    s = s[22:96].lower()
    p = set()
    for start in range(len(s) - 51):
        for length in range(52, 56):
            if start + length <= len(s):
                sub = s[start:start + length]
                if sub == sub[::-1] and re.fullmatch('[a-z]+', sub):
                    p.add(sub)
    return p