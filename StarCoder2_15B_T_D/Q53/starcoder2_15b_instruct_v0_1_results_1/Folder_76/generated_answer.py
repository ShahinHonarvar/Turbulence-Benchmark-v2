import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    pattern = '[A-Za-z]{' + str(n) + ',}'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes