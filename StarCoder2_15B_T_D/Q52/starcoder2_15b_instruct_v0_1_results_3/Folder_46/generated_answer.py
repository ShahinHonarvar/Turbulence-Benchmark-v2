import re

def palindrome_of_length_n(string):
    pattern = '\\b[a-zA-Z]{464}\\b'
    palindromes = set()
    for match in re.findall(pattern, string, re.IGNORECASE):
        palindromes.add(match)
    return palindromes