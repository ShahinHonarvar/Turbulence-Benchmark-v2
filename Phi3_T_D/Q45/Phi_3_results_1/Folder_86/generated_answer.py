from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(text):
    substring = text[6:10].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    valid_chars = english_letters.intersection(substring)
    palindromes = {''.join(p) for p in permutations(valid_chars, 4)}
    return {p for p in palindromes if is_palindrome(p)}