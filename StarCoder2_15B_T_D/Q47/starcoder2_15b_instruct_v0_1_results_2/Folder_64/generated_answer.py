import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[:8]
    pattern = '[a-zA-Z]{' + str(4) + ',' + str(5) + '}'
    matches = re.findall(pattern, substring, re.IGNORECASE)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes