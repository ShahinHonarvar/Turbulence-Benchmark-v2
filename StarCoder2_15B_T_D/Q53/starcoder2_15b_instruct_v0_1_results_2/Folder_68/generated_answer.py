import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    pattern = '\\b[a-z]{21,}\\b'
    matches = re.findall(pattern, s)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes