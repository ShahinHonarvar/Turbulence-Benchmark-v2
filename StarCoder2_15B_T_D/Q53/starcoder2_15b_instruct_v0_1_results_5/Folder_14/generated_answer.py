import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    pattern = re.compile('[a-z]{13,}')
    matches = pattern.findall(s)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes