from itertools import product

def expand_around_center(s, l, r):
    count = 0
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        count += 1
        if count >= 54:
            yield s[l:r + 1]
        l -= 1
        r += 1

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for p in expand_around_center(s, i, i):
            palindromes.add(p)
        for p in expand_around_center(s, i, i + 1):
            palindromes.add(p)
    return palindromes