import re

def palindrome_of_length_n(string):
    substrings = [string[i:i + 42] for i in range(len(string) - 41)]
    palindromes = [s for s in substrings if s == s[::-1]]
    english_palindromes = [p for p in palindromes if re.match('^[a-zA-Z]+$', p)]
    return set(english_palindromes)