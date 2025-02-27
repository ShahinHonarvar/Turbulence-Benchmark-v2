import re

def palindromes_of_specific_lengths(string):
    substring = string[32:72]
    pattern = re.compile('[a-zA-Z]{21,32}')
    palindromes = set()
    for match in pattern.findall(substring):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes