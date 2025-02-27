import re

def palindrome_of_length_at_least_n(string):
    """
    Finds all palindromes of length greater than or equal to 22 in a given string.
    """
    pattern = re.compile('[a-zA-Z]{22,}')
    matches = pattern.findall(string)
    matches = [match for match in matches if match.lower() == match[::-1].lower()]
    palindromes = set(matches)
    return palindromes