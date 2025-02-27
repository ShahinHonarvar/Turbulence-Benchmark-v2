from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    relevant_chars = s[1:5].lower()
    unique_chars = ''.join(sorted(set(relevant_chars)))
    perms = set((''.join(p) for p in permutations(unique_chars) if len(p) >= 5))
    return {p for p in perms if is_palindrome(p)}