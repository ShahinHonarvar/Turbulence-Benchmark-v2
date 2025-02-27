import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(14) + ',' + str(39) + '}'
    string = string[34:91]
    palindromes = set()
    for match in re.findall(pattern, string, flags=re.IGNORECASE):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes