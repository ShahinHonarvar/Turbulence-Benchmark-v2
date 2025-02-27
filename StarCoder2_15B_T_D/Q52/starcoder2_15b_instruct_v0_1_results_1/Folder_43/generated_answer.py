import re

def palindrome_of_length_n(string):
    pattern = '[a-zA-Z]{' + str(n) + '}'
    substrings = re.findall(pattern, string, re.IGNORECASE)
    palindromes = set((substring for substring in substrings if substring == substring[::-1]))
    return palindromes