from itertools import permutations

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindromes_between_indices(text):
    substring = text[2:10]
    unique_letters = ''.join(sorted(set(substring.lower()), key=substring.lower().index))
    possible_permutations = set((''.join(p) for p in permutations(unique_letters, 7)))
    return {p for p in possible_permutations if is_palindrome(p)}