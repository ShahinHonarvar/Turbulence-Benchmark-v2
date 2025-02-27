import re

def palindrome_of_length_at_least_n(string):
    """
    Finds all palindromes of length greater than or equal to 24 in a given string.
    """
    palindromes = set()
    string = string.lower()
    pattern = '\\b[a-z]{24,}\\b'
    matches = re.findall(pattern, string)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes