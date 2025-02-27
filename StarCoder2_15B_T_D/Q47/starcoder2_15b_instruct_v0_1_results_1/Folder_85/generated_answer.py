import re

def palindromes_of_specific_lengths(s):
    s = s[29:99]
    pattern = re.compile('[a-zA-Z]{6,9}')
    matches = pattern.findall(s)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes