import itertools
import string

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindromes_between_indices(s):
    start, end = (4, 8)
    possible_letters = [char.lower() for char in s[start:end + 1] if char.isalpha()]
    possible_permutations = set((''.join(p) for l in range(4, len(possible_letters) + 1) for p in itertools.permutations(possible_letters, l)))
    return set(filter(is_palindrome, possible_permutations))