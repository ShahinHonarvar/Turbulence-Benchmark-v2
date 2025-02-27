import re

def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    pattern = re.compile('[a-z]{76}')
    matches = pattern.findall(s)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes