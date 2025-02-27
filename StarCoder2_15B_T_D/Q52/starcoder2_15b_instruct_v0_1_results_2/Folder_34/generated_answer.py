import re

def palindrome_of_length_n(string):
    """
    Returns the set of all palindromes of length 33 as substrings of the given string.
    Each palindrome should only consist of English letters. The search is case-insensitive.
    """
    substrings = [string[i:i + 33] for i in range(len(string) - 32)]
    palindromes = [substring for substring in substrings if substring == substring[::-1] and re.match('^[a-zA-Z]+$', substring)]
    return set(palindromes)