import re

def palindrome_of_length_n(string):
    length = 28
    substrings = [string[i:i + length] for i in range(len(string) - length + 1)]
    palindromes = {substring for substring in substrings if substring == substring[::-1] and re.match('^[a-zA-Z]+$', substring)}
    return palindromes