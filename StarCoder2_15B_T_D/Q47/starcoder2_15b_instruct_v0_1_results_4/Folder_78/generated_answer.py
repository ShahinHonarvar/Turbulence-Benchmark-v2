import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[15:73]
    pattern = re.compile('[a-zA-Z]{19,55}')
    matches = pattern.findall(substring)
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes