import re

def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    substring = s[10:75]
    valid_palindromes = set()
    pattern = re.compile('[a-zA-Z]+')
    matches = pattern.findall(substring)
    for match in matches:
        if 6 <= len(match) <= 8 and is_palindrome(match.lower()):
            valid_palindromes.add(match)
    return valid_palindromes