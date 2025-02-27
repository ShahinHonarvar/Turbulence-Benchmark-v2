import re

def palindrome_of_length_at_least_n(string, n=149):
    pattern = re.compile('[a-zA-Z]{149,}')
    matches = pattern.findall(string)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes