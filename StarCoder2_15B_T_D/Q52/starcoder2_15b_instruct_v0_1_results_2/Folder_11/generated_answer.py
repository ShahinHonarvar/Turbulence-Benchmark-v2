import re

def palindrome_of_length_n(string):
    """
    Find all palindromes of length 77 in a given string.
    """
    string = string.lower()
    pattern = '[a-z]{' + str(77) + '}'
    palindromes = set(re.findall(pattern, string))
    return palindromes