import re

def is_palindrome(s: str) -> bool:
    return s == s[::-1] and s.isalpha()

def palindromes_of_specific_lengths(input_string: str) -> set:
    substring = input_string[20:75]
    valid_palindromes = {substring[i:i + length] for length in range(36, 43) for i in range(len(substring) - length + 1) if is_palindrome(substring[i:i + length])}
    return {p.upper() for p in valid_palindromes}