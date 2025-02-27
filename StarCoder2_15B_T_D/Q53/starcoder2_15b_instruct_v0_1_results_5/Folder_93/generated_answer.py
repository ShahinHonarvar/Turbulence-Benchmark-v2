import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    pattern = re.compile('[a-z]{90,}')
    matches = pattern.finditer(string)
    palindromes = set()
    for match in matches:
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes