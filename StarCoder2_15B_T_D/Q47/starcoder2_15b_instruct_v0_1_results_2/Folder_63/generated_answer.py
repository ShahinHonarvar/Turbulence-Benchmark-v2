import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(26) + ',' + str(31) + '}'
    substring = string[33:86]
    matches = re.findall(pattern, substring, flags=re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes