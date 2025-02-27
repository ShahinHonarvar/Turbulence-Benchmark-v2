import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    pattern = re.compile('[a-z]{85}')
    matches = pattern.findall(string)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes