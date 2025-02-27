import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[100:301]
    pattern = '[a-zA-Z]{' + str(50) + ',' + str(100) + '}'
    for match in re.findall(pattern, substring, re.IGNORECASE):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes