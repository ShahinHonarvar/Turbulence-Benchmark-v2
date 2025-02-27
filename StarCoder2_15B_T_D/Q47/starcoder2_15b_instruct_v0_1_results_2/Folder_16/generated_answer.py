import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[15:87]
    pattern = '[a-zA-Z]{' + str(51) + ',' + str(60) + '}'
    matches = re.findall(pattern, substring, flags=re.IGNORECASE)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes