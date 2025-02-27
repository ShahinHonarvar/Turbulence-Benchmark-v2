import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    pattern = re.compile('[a-z]{62,}')
    matches = pattern.finditer(string)
    for match in matches:
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes