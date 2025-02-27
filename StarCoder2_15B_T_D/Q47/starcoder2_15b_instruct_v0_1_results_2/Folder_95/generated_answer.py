import re

def palindromes_of_specific_lengths(text):
    pattern = '[A-Za-z]{20,21}'
    matches = re.findall(pattern, text[12:57])
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes