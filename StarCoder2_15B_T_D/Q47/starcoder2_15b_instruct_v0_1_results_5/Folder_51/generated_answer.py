import re

def palindromes_of_specific_lengths(string):
    pattern = re.compile('[a-zA-Z]{3,4}', re.IGNORECASE)
    palindromes = set()
    for match in pattern.finditer(string[2:9]):
        palindromes.add(match.group())
    return palindromes