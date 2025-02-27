import re

def palindromes_of_specific_lengths(string: str) -> set:
    substring = string[3:301]
    pattern = re.compile('[a-zA-Z]{' + str(30) + ',' + str(300) + '}')
    matches = pattern.findall(substring)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes