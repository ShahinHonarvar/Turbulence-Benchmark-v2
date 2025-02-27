import re

def palindrome_of_length_at_least_n(s):
    pattern = re.compile('[A-Za-z]{89,}')
    matches = pattern.findall(s)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes