from string import ascii_letters
from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[5:10].lower()
    letters = ''.join(filter(lambda c: c in ascii_letters, substring))
    palindromes = {''.join(p) for p in permutations(letters, len(letters)) if is_palindrome(p)}
    return {p for p in palindromes if len(p) >= 6}