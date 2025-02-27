import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[:7]
    pattern = '[a-zA-Z]{' + str(3) + ',' + str(6) + '}'
    for match in re.findall(pattern, substring, flags=re.IGNORECASE):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes