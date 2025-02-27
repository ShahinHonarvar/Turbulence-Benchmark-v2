from itertools import permutations

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindromes_between_indices(s):
    return set([''.join(p) for p in permutations(s[1:5].lower()) if is_palindrome(p) and len(p) >= 3])