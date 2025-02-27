import itertools

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[4:7]]
    permutations = set((''.join(p) for p in itertools.permutations(chars)))
    return set(filter(is_palindrome, permutations))