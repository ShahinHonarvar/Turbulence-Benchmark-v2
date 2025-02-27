import re

def palindromes_of_specific_lengths(s):
    s = s[44:100].lower()
    p = set()
    for i in range(len(s)):
        for j in range(i + 13, min(i + 43, len(s) + 1)):
            if s[i:j] == s[i:j][::-1] and re.fullmatch('[a-z]+', s[i:j]):
                p.add(s[i:j])
    return p