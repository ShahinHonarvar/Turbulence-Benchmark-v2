import re

def is_palindrome(s):
    return s == s[::-1] and all(('a' <= c.lower() <= 'z' for c in s))

def palindrome_of_length_at_least_n(input_str):
    input_str = input_str.lower()
    palindromes = set()
    for i in range(len(input_str)):
        for j in range(i + 140, len(input_str) + 1):
            substring = input_str[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes