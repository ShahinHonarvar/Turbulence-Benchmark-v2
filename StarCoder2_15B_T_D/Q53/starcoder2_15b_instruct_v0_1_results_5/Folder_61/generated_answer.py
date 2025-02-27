import re

def palindrome_of_length_at_least_n(string):
    """
    Returns the set of all palindromes of the length greater than or equal to 5 that exist in the given string.
    """
    regex = re.compile('[a-zA-Z]{5,}')
    matches = regex.findall(string)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes