import re

def palindrome_of_length_at_least_n(string):
    pattern = re.compile('[a-zA-Z]{63,}')
    palindromes = set()
    for match in pattern.finditer(string):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes