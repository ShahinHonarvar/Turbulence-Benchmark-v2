import re

def palindrome_of_length_n(text):
    pattern = re.compile('[a-zA-Z]{255}')
    palindromes = set()
    for match in pattern.finditer(text):
        palindromes.add(match.group().lower())
    return palindromes