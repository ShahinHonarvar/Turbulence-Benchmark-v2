import re

def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        yield s[l:r + 1]
        l -= 1
        r += 1

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i, _ in enumerate(s):
        for p in expand_around_center(s, i, i):
            if len(p) >= 93:
                palindromes.add(p)
        for p in expand_around_center(s, i, i + 1):
            if len(p) >= 94:
                palindromes.add(p)
    return palindromes