import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(52) + ',' + str(56) + '}'
    matches = re.findall(pattern, string[26:88])
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes