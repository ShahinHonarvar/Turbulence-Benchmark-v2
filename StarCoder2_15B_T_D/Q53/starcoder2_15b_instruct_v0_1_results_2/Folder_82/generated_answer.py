import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    pattern = '[A-Za-z]{' + str(n) + ',}'
    for match in re.findall(pattern, string, flags=re.IGNORECASE):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes