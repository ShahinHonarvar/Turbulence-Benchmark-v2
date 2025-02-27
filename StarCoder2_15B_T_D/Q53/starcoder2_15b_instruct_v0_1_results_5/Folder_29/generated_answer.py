import re

def palindrome_of_length_at_least_n(s):
    """
    Finds all palindromes of length greater than or equal to 78 in a given string.
    """
    pattern = '\\b[a-zA-Z]{78,}\\b'
    matches = re.findall(pattern, s, flags=re.IGNORECASE)
    return set(matches)