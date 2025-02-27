import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    pattern = re.compile('[a-zA-Z]{74,}')
    matches = pattern.findall(s)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes