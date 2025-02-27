import re

def palindromes_of_specific_lengths(string):
    substring = string[1:10]
    pattern = '[a-zA-Z]{' + str(3) + ',' + str(7) + '}'
    matches = re.findall(pattern, substring, flags=re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes