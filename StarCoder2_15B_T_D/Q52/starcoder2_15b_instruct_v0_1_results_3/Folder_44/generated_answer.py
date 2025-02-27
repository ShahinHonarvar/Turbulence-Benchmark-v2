import re

def palindrome_of_length_n(string):
    substrings = [string[i:i + 445] for i in range(len(string) - 444)]
    palindromes = [substring for substring in substrings if substring == substring[::-1]]
    filtered_palindromes = [palindrome for palindrome in palindromes if re.match('^[a-zA-Z]+$', palindrome)]
    return set(filtered_palindromes)