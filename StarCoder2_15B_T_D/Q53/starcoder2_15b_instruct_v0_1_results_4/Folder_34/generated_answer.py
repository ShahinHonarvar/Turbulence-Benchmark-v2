import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    pattern = '\\b[a-z]{68,}\\b'
    for match in re.finditer(pattern, string.lower()):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes