import re

def palindrome_of_length_at_least_n(string):
    """
    Returns a set of all palindromes of length greater than or equal to 62 in a given string.
    """
    pattern = re.compile('[a-zA-Z]{62,}')
    matches = pattern.findall(string)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes