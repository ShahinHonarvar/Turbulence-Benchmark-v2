import re

def palindrome_of_length_n(string):
    """
    Returns the set of all palindromes of length 255 as substrings of the given string.
    Each palindrome should only consist of English letters. If there is no palindrome
    of the specified length as a substring of the given string, the function returns
    an empty set. The function finds the palindromes in a case-insensitive manner.
    """
    pattern = '[a-zA-Z]{' + str(255) + '}'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    palindromes = set((m for m in matches if m == m[::-1]))
    return palindromes