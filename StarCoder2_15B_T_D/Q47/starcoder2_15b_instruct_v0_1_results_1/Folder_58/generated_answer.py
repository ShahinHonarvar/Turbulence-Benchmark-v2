import re

def palindromes_of_specific_lengths(string):
    pattern = re.compile('[a-zA-Z]{109,126}', re.IGNORECASE)
    palindromes = set()
    for match in pattern.finditer(string[125:284]):
        palindromes.add(match.group())
    return palindromes