from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    sub = s[1:6].lower()
    letters = ''.join(sorted(set(sub)))
    perms = set(permutations(letters, 5))
    return set((''.join(p) for p in perms if is_palindrome(''.join(p))))