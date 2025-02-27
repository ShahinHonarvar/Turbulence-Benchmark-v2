import re

def palindrome_of_length_n(string):
    """
    Returns a set of all palindromes of length 54 as substrings of the given string.
    """
    pattern = '[a-zA-Z]{' + str(54) + '}'
    palindromes = set(re.findall(pattern, string, flags=re.IGNORECASE))
    return palindromes