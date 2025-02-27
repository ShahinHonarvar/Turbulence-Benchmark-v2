import re

def palindrome_of_length_n(string):
    """
    Finds all palindromes of length 35 as substrings of the given string.
    """
    pattern = re.compile('[a-zA-Z]{35}')
    matches = pattern.findall(string)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes