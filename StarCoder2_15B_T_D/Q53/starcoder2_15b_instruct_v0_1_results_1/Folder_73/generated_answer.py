import re

def palindrome_of_length_at_least_n(string):
    pattern = re.compile('[a-zA-Z]{94,}')
    matches = pattern.finditer(string)
    palindromes = set()
    for match in matches:
        palindromes.add(match.group().lower())
    return palindromes