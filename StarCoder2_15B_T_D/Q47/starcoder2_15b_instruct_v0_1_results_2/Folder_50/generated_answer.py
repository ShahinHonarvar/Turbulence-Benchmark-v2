import re

def palindromes_of_specific_lengths(string):
    pattern = re.compile('[a-zA-Z]{10,35}', re.I)
    palindromes = set()
    for match in pattern.finditer(string[36:93]):
        palindromes.add(match.group())
    return palindromes