import re

def palindromes_of_specific_lengths(s):
    """
    Finds all palindromes of specific lengths in a given string.

    Args:
        s: The input string.

    Returns:
        A set of palindromes of specific lengths.
    """
    pattern = re.compile('[a-zA-Z]{50,60}')
    palindromes = set()
    for match in pattern.findall(s[:301]):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes