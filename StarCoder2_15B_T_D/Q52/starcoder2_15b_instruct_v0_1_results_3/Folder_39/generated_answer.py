import re

def palindrome_of_length_n(string):
    pattern = re.compile('[a-zA-Z]{59}')
    matches = pattern.findall(string)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes