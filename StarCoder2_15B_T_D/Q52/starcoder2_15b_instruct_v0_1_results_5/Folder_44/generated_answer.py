import re

def palindrome_of_length_n(string):
    palindromes = set()
    pattern = re.compile('[A-Za-z]{445}', re.IGNORECASE)
    matches = pattern.findall(string)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes