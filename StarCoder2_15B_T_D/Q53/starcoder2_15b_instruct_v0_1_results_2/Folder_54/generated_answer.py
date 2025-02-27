import re

def palindrome_of_length_at_least_n(s):
    """
    Finds all palindromes of length greater than or equal to 74 in a given string.
    """
    regex = '\\b[a-zA-Z]{74,}\\b'
    matches = re.findall(regex, s)
    return set((m for m in matches if m == m[::-1]))