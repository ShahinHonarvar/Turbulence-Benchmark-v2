from itertools import permutations
import string

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = ''.join(filter(lambda c: c in string.ascii_letters, s[:5])).lower()
    unique_chars = ''.join(set(s))
    result = set()
    for p in permutations(unique_chars, 4):
        candidate_palindrome = ''.join(p) + ''.join(reversed(p))
        if candidate_palindrome.startswith(s[:2]):
            result.add(candidate_palindrome)
    return result