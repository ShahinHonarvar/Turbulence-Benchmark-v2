import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(12) + ',' + str(220) + '}'
    matches = re.findall(pattern, string[12:123], flags=re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes