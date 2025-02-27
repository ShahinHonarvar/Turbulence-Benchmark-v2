import re

def palindrome_of_length_n(string):
    palindromes = set()
    pattern = re.compile('[a-zA-Z]{88}', re.IGNORECASE)
    for match in pattern.finditer(string):
        palindromes.add(match.group().lower())
    return palindromes