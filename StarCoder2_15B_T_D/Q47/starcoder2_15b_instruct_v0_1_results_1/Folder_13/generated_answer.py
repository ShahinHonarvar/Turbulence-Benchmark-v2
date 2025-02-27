import re

def palindromes_of_specific_lengths(string):
    pattern = re.compile('[a-zA-Z]{57,60}')
    substring = string[13:96]
    matches = pattern.findall(substring)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes