import re

def palindromes_of_specific_lengths(string):
    substring = string[18:66]
    pattern = '[a-zA-Z]{' + str(23) + ',' + str(36) + '}'
    palindromes = set()
    for length in range(23, 37):
        matches = re.findall(pattern, substring, flags=re.IGNORECASE)
        for match in matches:
            if match == match[::-1]:
                palindromes.add(match)
    return palindromes