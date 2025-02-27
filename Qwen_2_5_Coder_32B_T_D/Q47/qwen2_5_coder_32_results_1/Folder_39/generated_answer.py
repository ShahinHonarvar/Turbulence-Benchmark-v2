import re

def palindromes_of_specific_lengths(s):
    s = s[31:92].lower()
    r = set()
    for i in range(len(s) - 50 + 1):
        for l in range(50, 54):
            if i + l <= len(s):
                sub = s[i:i + l]
                if sub == sub[::-1] and re.fullmatch('[a-z]+', sub):
                    r.add(sub)
    return r