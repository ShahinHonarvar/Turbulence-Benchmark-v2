from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[3:7]
    all_perms = set((''.join(p) for p in permutations(substring.lower())))
    palindromes = {p for p in all_perms if len(p) >= 4 and is_palindrome(p)}
    return palindromes