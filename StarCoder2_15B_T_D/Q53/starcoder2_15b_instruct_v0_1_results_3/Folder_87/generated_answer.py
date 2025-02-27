import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    pattern = '\\b[a-z]{18,}\\b'
    matches = re.findall(pattern, s)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes