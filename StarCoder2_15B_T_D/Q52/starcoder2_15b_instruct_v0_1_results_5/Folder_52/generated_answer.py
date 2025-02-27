import re

def palindrome_of_length_n(string):
    """
    Returns the set of all palindromes of the length equal to 423,
    where each palindrome is a substring of the given string.
    """
    palindromes = set()
    pattern = '[a-zA-Z]{423}'
    matches = re.findall(pattern, string)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes