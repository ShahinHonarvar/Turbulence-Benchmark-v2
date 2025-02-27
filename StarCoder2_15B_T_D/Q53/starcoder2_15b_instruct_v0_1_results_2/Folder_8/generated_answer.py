import re

def palindrome_of_length_at_least_n(s):
    s_lower = s.lower()
    pattern = '[a-z]{' + str(n) + ',}'
    matches = re.findall(pattern, s_lower)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes