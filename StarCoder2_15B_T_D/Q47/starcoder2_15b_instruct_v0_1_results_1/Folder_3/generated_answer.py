import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(49) + ',' + str(51) + '}'
    matches = re.findall(pattern, string[27:96], flags=re.IGNORECASE)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes