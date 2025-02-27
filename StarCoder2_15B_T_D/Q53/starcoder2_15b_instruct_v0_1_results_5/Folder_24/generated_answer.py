import re

def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s) - 52):
        for j in range(i + 53, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring) and re.match('^[a-zA-Z]+$', substring):
                palindromes.add(substring)
    return palindromes