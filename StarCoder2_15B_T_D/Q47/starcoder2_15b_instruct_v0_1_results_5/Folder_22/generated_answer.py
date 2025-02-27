import re

def palindromes_of_specific_lengths(string):
    substring = string[100:201]
    pattern = re.compile('(?i)[a-z]{5,10}')
    matches = pattern.findall(substring)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes