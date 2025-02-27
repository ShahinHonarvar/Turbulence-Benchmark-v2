import re

def palindromes_of_specific_lengths(string):
    substring = string[17:96]
    pattern = '[a-zA-Z]{' + str(13) + ',' + str(49) + '}'
    palindromes = set()
    for length in range(13, 50):
        matches = re.findall(pattern, substring, flags=re.IGNORECASE)
        for match in matches:
            if match == match[::-1]:
                palindromes.add(match)
    return palindromes