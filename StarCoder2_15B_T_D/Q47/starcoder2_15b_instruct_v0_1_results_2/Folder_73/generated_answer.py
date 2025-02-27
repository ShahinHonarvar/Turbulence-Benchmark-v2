import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(22) + ',' + str(33) + '}'
    substring = string[21:63]
    matches = re.findall(pattern, substring, flags=re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes