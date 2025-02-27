import re

def palindrome_of_length_n(string):
    pattern = re.compile('[a-zA-Z]{366}')
    palindromes = set()
    for match in pattern.finditer(string):
        palindromes.add(match.group().lower())
    return palindromes