from itertools import permutations

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindromes_between_indices(text: str) -> set:
    english_chars = [char.lower() for char in text.lower() if 'a' <= char.lower() <= 'z']
    english_chars_to_use = english_chars[:7]
    possible_perms = set((''.join(p) for p in permutations(english_chars_to_use)))
    return {perm for perm in possible_perms if is_palindrome(perm)}