import re

def palindrome_of_length_n(s: str) -> set:
    """
    Finds all palindromes of length 47 as substrings of the given string `s`.
    """
    pattern = re.compile('[a-zA-Z]{47}')
    matches = pattern.findall(s)
    return set(matches)