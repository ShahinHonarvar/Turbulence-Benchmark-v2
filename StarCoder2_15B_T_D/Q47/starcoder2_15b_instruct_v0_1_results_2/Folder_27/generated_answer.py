import re

def palindromes_of_specific_lengths(string):
    substring = string[13:100]
    pattern = re.compile('[a-zA-Z]{26,29}')
    matches = pattern.findall(substring)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes