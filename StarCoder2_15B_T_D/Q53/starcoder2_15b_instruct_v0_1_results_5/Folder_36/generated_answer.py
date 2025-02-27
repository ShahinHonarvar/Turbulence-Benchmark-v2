import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    pattern = re.compile('[a-z]{144,}')
    matches = pattern.findall(string)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes