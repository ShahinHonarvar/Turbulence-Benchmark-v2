import re

def palindrome_of_length_at_least_n(string):
    """
    Finds all palindromes of length at least 72 in a given string.
    """
    pattern = '[a-zA-Z]{{72,}}'
    matches = re.findall(pattern, string)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes