import re

def palindrome_of_length_n(string):
    substrings = [string[i:i + 41] for i in range(len(string) - 40)]
    palindromes = [substring for substring in substrings if re.match('^([A-Za-z]{41})$', substring) and substring == substring[::-1]]
    return set(palindromes)