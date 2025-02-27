import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(12) + ',' + str(220) + '}'
    palindromes = set()
    matches = re.finditer(pattern, string[12:122])
    for match in matches:
        substring = match.group()
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes