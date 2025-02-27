import re

def palindromes_of_specific_lengths(string):
    """
    Returns a set of all palindromes with specific lengths in a given string.
    """
    regex = re.compile('[a-zA-Z]{100,169}')
    matches = regex.findall(string[103:277])
    palindromes = set((match for match in matches if match.lower() == match[::-1]))
    return palindromes