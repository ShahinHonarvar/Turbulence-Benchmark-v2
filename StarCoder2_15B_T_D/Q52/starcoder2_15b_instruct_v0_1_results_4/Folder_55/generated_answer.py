import re

def palindrome_of_length_n(text):
    """
    Find all palindromes of length 97 in a given text,
    where each palindrome is a substring of the text.
    """
    pattern = '(.{97})'
    matches = re.findall(pattern, text, re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes