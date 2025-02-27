import re

def palindrome_of_length_n(string):
    substrings = [string[i:i + 23] for i in range(len(string) - 22)]
    palindromes = [substring for substring in substrings if substring == substring[::-1]]
    return set(filter(lambda x: re.match('^[a-zA-Z]+$', x), palindromes))