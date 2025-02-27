from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[5:9]
    unique_chars = set([c.lower() for c in substring if c.isalpha()])
    perms = set([''.join(p) for p in permutations(unique_chars)])
    return {p for p in perms if len(p) >= 3 and is_palindrome(p)}