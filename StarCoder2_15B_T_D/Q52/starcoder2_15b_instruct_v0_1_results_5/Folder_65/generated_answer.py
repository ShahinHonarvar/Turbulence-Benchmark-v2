import re

def palindrome_of_length_n(string):
    substrings = [string[i:i + 35] for i in range(len(string) - 34)]
    palindromes = [substring for substring in substrings if substring == substring[::-1]]
    return set(palindromes)