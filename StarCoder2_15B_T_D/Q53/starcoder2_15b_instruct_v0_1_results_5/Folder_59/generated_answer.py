import re

def palindrome_of_length_at_least_n(string):
    """
    Returns the set of all palindromes of length greater than or equal to 20 that exist in the given string.
    Each palindrome should only consist of English letters. If no such palindromes exist in the given string,
    the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    pattern = re.compile('\\b[a-zA-Z]{20,}\\b')
    matches = pattern.findall(string)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes