import re

def palindromes_of_specific_lengths(s):
    s = s[39:95].lower()
    p = set()
    for i in range(len(s)):
        for j in range(i + 14, min(i + 53, len(s) + 1)):
            sub = s[i:j]
            if sub == sub[::-1] and re.fullmatch('[a-z]+', sub):
                p.add(sub)
    return p