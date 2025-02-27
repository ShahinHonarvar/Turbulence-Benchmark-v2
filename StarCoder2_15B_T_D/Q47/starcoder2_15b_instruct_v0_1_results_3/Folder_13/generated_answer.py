import re

def palindromes_of_specific_lengths(string):
    substring = string[13:96]
    regex = re.compile('[a-zA-Z]{57,60}')
    matches = regex.findall(substring)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes