import re

def palindrome_of_length_at_least_n(s):
    pattern = re.compile('[a-zA-Z]{31,}')
    matches = pattern.findall(s)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes