import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    regex = re.compile(pattern, re.IGNORECASE)
    palindromes = set()
    for match in regex.finditer(string):
        palindromes.add(match.group().lower())
    return palindromes