import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(34) + ',' + str(55) + '}'
    substring = string[30:96]
    palindromes = set()
    for match in re.findall(pattern, substring, re.IGNORECASE):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes