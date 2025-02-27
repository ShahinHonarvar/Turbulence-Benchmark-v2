import re

def palindrome_of_length_n(string):
    substrings = [string[i:i + 90] for i in range(len(string) - 89)]
    palindromes = [substring for substring in substrings if substring == substring[::-1]]
    filtered_palindromes = list(filter(lambda x: re.match('^[a-zA-Z]+$', x), palindromes))
    return set(filtered_palindromes)