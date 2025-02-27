import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = 28
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    matches = re.findall(pattern, s, re.IGNORECASE)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes