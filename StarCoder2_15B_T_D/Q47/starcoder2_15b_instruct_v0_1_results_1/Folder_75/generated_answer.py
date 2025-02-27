import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(23) + ',' + str(39) + '}'
    substring = string[31:75]
    for match in re.findall(pattern, substring, re.IGNORECASE):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes