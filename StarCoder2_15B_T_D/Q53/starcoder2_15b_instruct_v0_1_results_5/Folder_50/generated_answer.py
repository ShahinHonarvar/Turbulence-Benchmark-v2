import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    pattern = re.compile('([a-zA-Z]{91,})(\\1)', re.IGNORECASE)
    for match in pattern.finditer(string):
        palindromes.add(match.group(1).lower())
    return palindromes