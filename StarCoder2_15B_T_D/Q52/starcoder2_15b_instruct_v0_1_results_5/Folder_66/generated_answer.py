import re

def palindrome_of_length_n(string):
    pattern = re.compile('[a-zA-Z]{' + str(n) + '}', re.I)
    palindromes = set()
    for match in re.finditer(pattern, string):
        palindromes.add(match.group().lower())
    return palindromes