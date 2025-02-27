import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(40) + ',' + str(47) + '}'
    matches = re.findall(pattern, string[45:99])
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes