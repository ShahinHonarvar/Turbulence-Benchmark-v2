import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[100:296]
    pattern = '[A-Za-z]{' + str(136) + ',' + str(160) + '}'
    for match in re.findall(pattern, substring, flags=re.I):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes