import re

def palindrome_of_length_at_least_n(s, n=20):
    s = s.lower()
    pattern = re.compile('[a-z]+')
    matches = pattern.findall(s)
    palindromes = set()
    for match in matches:
        if len(match) >= n and match == match[::-1]:
            palindromes.add(match)
    return palindromes