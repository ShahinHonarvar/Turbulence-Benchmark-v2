from itertools import permutations
    import string

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:6] if c.lower() in string.ascii_lowercase]
    perms = set(permutations(letters, len(letters)))
    return {''.join(p) for p in perms if is_palindrome(''.join(p)) and len(''.join(p)) >= 6}