import re

def palindromes_of_specific_lengths(string):
    substring = string[103:277]
    pattern = re.compile('[a-zA-Z]{100,170}')
    palindromes = set()
    for match in pattern.finditer(substring):
        palindromes.add(match.group().lower())
    return palindromes