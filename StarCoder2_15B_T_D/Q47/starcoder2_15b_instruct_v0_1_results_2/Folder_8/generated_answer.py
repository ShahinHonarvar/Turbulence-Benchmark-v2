import re

def palindromes_of_specific_lengths(string):
    substring = string[17:73]
    pattern = re.compile('[a-zA-Z]{50,51}')
    matches = pattern.findall(substring)
    palindromes = set()
    for match in matches:
        if match.lower() == match.lower()[::-1]:
            palindromes.add(match)
    return palindromes