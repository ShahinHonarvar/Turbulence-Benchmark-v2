import re

def palindrome_of_length_at_least_n(string):
    pattern = '[A-Za-z]{32,}'
    matches = re.findall(pattern, string)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes