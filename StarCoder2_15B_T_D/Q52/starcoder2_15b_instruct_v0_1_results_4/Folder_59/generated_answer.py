import re

def palindrome_of_length_n(string):
    pattern = re.compile('[a-zA-Z]{39}')
    matches = pattern.findall(string)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes