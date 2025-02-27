import re

def palindromes_of_specific_lengths(string):
    substring = string[12:93]
    regex = re.compile('[a-zA-Z]{17,66}')
    matches = regex.findall(substring)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes