import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(14) + ',' + str(52) + '}'
    matches = re.findall(pattern, string[39:95])
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes