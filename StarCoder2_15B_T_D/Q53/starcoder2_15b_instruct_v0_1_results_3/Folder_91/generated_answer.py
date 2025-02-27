import re

def palindrome_of_length_at_least_n(s, n=7):
    pattern = re.compile('[a-zA-Z]{7,}')
    palindromes = set()
    for match in pattern.findall(s):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes