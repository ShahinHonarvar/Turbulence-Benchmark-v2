import re

def palindromes_of_specific_lengths(s):
    pattern = '[a-zA-Z]{' + str(32) + ',' + str(34) + '}'
    matches = re.findall(pattern, s[23:83], flags=re.IGNORECASE)
    palindromes = set()
    for match in matches:
        reversed_match = match[::-1]
        if match.lower() == reversed_match.lower():
            palindromes.add(match)
    return palindromes