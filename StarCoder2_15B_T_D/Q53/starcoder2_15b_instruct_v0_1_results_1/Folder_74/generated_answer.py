import re

def palindrome_of_length_at_least_n(s):
    pattern = '[A-Za-z]{' + str(n) + ',}'
    matches = re.findall(pattern, s, flags=re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes