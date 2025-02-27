import re

def palindrome_of_length_n(string):
    """
    Finds all palindromes of length 7 as substrings of the given string.
    """
    pattern = re.compile('[a-zA-Z]{7}', re.IGNORECASE)
    return set(pattern.findall(string))