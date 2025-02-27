from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    letters = {c.lower() for c in s[4:7]}
    palindromes = set((''.join(p) for p in permutations(letters) if len(p) >= 4 and is_palindrome(''.join(p))))
    return palindromes