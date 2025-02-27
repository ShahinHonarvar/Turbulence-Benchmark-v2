import re

def palindromes_of_specific_lengths(s):
    s = s[200:301].lower()
    p = set()
    for i in range(len(s)):
        for j in range(i + 9, min(i + 51, len(s))):
            sub = s[i:j + 1]
            if sub == sub[::-1] and re.fullmatch('[a-z]+', sub):
                p.add(sub)
    return p