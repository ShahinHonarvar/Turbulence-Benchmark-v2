import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[30:85]
    pattern = '[a-zA-Z]{' + str(12) + ',' + str(20) + '}'
    matches = re.findall(pattern, substring, flags=re.IGNORECASE)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes