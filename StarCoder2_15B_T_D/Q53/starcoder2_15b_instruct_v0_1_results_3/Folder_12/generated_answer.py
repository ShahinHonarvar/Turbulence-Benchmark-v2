import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    pattern = re.compile('(?i)(?=(\\w{51,}))\\1')
    for match in pattern.finditer(string):
        palindromes.add(match.group(1))
    return palindromes