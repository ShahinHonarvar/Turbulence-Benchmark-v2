import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(27) + ',' + str(58) + '}'
    palindromes = set()
    for match in re.findall(pattern, string[26:91]):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes