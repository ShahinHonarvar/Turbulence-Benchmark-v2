import re

def palindromes_of_specific_lengths(s):
    s = s[26:88].lower()
    r = set()
    for i in range(len(s)):
        for j in range(52, 57):
            if i + j <= len(s):
                sub = s[i:i + j]
                if sub == sub[::-1] and re.fullmatch('[a-z]+', sub):
                    r.add(sub)
    return r