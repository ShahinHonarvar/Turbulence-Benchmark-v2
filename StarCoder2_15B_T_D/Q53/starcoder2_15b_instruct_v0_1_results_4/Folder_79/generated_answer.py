import re

def palindrome_of_length_at_least_n(string):
    pattern = '[A-Za-z]{' + str(n) + ',}'
    palindromes = set()
    for match in re.finditer(pattern, string, re.IGNORECASE):
        if match.group().lower() == match.group()[::-1].lower():
            palindromes.add(match.group())
    return palindromes