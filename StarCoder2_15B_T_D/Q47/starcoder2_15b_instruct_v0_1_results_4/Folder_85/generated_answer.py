import re

def palindromes_of_specific_lengths(string):
    substring = string[29:99]
    pattern = '[a-zA-Z]{' + str(6) + ',' + str(9) + '}'
    palindromes = set()
    for match in re.findall(pattern, substring, flags=re.IGNORECASE):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes