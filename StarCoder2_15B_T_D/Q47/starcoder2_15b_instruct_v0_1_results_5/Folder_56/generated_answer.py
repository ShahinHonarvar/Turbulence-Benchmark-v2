import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[1:10]
    pattern = '[a-zA-Z]{' + str(3) + ',' + str(7) + '}'
    for match in re.findall(pattern, substring, flags=re.IGNORECASE):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes