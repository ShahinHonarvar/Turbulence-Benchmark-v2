import re

def palindrome_of_length_at_least_n(text):
    pattern = re.compile('[A-Za-z]{141,}')
    palindromes = set()
    for match in pattern.finditer(text):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes