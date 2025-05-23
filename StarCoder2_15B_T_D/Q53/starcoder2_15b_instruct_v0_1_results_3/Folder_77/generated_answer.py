import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    pattern = re.compile('[a-zA-Z]{149,}')
    for match in pattern.finditer(string):
        palindrome = match.group(0)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes