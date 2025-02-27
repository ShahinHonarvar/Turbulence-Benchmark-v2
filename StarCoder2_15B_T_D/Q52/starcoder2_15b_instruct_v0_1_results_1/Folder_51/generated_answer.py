import re

def palindrome_of_length_n(string):
    palindromes = set()
    n = 73
    regex = re.compile('[a-zA-Z]{' + str(n) + '}')
    for match in regex.finditer(string):
        palindromes.add(match.group().lower())
    return palindromes