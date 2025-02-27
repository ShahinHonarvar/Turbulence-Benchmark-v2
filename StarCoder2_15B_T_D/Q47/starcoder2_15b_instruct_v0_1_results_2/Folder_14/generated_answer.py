import re

def palindromes_of_specific_lengths(string):
    string = string[10:75]
    pattern = '[a-zA-Z]{' + str(6) + ',' + str(8) + '}'
    matches = re.findall(pattern, string, re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes