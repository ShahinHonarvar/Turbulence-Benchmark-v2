import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    pattern = '[a-z]{' + str(45) + ',}'
    palindromes = set()
    matches = re.findall(pattern, s)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes