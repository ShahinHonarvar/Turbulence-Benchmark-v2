from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    subset = s[0:6].lower()
    unique_perms = set((''.join(p) for p in permutations(subset) if len(p) >= 5))
    return {p for p in unique_perms if is_palindrome(p)}