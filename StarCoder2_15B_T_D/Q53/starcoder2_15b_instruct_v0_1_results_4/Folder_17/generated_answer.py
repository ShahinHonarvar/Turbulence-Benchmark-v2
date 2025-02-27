import re

def palindrome_of_length_at_least_n(string):
    pattern = '\\b[a-zA-Z]{36,}\\b'
    palindromes = set()
    for match in re.finditer(pattern, string):
        palindrome = match.group(0).lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes