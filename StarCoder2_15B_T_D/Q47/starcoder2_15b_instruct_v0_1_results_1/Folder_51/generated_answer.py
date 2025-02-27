import re

def palindromes_of_specific_lengths(string):
    pattern = re.compile('(?i)[a-z]{3,4}')
    palindromes = set()
    for match in pattern.finditer(string[2:9]):
        palindromes.add(match.group())
    return palindromes