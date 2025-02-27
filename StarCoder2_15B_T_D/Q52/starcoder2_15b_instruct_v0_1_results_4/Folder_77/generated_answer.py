import re

def palindrome_of_length_n(text):
    palindromes = set()
    pattern = re.compile('[a-zA-Z]{173}', re.IGNORECASE)
    for match in pattern.finditer(text):
        palindrome = match.group()
        palindromes.add(palindrome)
    return palindromes