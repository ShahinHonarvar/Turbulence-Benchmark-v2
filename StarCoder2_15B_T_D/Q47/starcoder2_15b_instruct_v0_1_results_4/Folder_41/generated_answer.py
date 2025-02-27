import re

def palindromes_of_specific_lengths(s):
    pattern = '[a-zA-Z]{' + str(3) + ',' + str(4) + '}'
    regex = re.compile(pattern, re.IGNORECASE)
    matches = regex.findall(s[1:8])
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes