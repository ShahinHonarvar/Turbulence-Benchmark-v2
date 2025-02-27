from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def create_palindromes(letters):
    palindromes = {''.join(p) for p in permutations(letters)}
    return {p for p in palindromes if is_palindrome(p)}

def palindromes_between_indices(input_str):
    substring = input_str[3:7]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    return create_palindromes(letters)