import re

def palindromes_of_specific_lengths(string):
    substring = string[10:71]
    pattern = '\\\\b[a-zA-Z]{24,52}\\\\b'
    matches = re.findall(pattern, substring, re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes