import re

def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    palindromes = set()
    length = 6
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if all((char.isalpha() for char in substring)) and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes