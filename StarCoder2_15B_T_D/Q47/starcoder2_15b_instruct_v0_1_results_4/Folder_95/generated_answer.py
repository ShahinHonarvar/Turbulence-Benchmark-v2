import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(20) + ',' + str(21) + '}'
    matches = re.finditer(pattern, string[12:57])
    for match in matches:
        if match.group().lower() == match.group()[::-1].lower():
            palindromes.add(match.group())
    return palindromes