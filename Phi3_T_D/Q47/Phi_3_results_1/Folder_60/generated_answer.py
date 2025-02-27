import re

def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    required_palindromes = set()
    substring = s[23:83]
    for length in range(32, 35):
        for i in range(len(substring) - length + 1):
            possible_palindrome = substring[i:i + length]
            if re.match('^[a-zA-Z]+$', possible_palindrome) and is_palindrome(possible_palindrome.lower()):
                required_palindromes.add(possible_palindrome.lower())
    return required_palindromes