import re

def palindrome_of_length_at_least_n(string):
    """
    Find all palindromes of length greater than or equal to 57 in a given string.
    """
    pattern = '\\b[A-Za-z]{57,}\\b'
    palindromes = set(re.findall(pattern, string, flags=re.IGNORECASE))
    return palindromes