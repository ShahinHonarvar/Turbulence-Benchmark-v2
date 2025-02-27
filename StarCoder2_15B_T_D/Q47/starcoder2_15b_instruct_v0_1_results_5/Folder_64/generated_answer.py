import re

def palindromes_of_specific_lengths(string):
    sub_string = string[:8]
    pattern = re.compile('[a-zA-Z]{4,5}')
    matches = pattern.findall(sub_string)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes