from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(input_string):
    substring = input_string[2:9]
    letters = sorted((s.lower() for s in substring if s.isalpha()))
    basis = ''.join(letters)
    valid_perms = {perm for perm in permutations(basis) if len(perm) >= 4 and is_palindrome(perm)}
    return set((''.join(perm).ljust(9, ' ') for perm in valid_perms))