import re

def palindrome_of_length_at_least_n(s):
    pattern = re.compile('\\b[a-z]{100,}\\b', re.IGNORECASE)
    palindromes = set()
    for match in pattern.finditer(s):
        palindromes.add(match.group())
    return palindromes