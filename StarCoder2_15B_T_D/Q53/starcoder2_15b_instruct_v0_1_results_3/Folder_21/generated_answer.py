import re

def palindrome_of_length_at_least_n(s):
    pattern = re.compile('[a-zA-Z]{112,}')
    palindromes = set()
    for match in pattern.finditer(s):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes