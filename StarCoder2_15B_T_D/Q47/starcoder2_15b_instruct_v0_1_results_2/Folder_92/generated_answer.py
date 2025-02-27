import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(3) + ',' + str(4) + '}'
    substring = string[:5]
    palindromes = set()
    for match in re.findall(pattern, substring, flags=re.IGNORECASE):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes