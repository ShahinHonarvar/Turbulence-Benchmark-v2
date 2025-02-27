import re

def palindromes_of_specific_lengths(s):
    s = s[127:289].lower()
    p = set()
    for i in range(len(s)):
        for j in range(119, 142):
            if i + j <= len(s):
                sub = s[i:i + j]
                if sub == sub[::-1] and re.fullmatch('[a-z]+', sub):
                    p.add(sub)
    return p