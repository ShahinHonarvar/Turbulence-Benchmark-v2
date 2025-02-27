import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(3) + ',' + str(5) + '}'
    matches = re.findall(pattern, string[0:11], flags=re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes