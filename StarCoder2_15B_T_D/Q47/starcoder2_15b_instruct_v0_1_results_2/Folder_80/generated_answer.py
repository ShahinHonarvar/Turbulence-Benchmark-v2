import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[35:89]
    pattern = '[a-zA-Z]{' + str(24) + ',' + str(33) + '}'
    for match in re.findall(pattern, substring, flags=re.IGNORECASE):
        if match.lower() == match[::-1].lower():
            palindromes.add(match.lower())
    return palindromes