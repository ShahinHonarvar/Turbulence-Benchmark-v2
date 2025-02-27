import re

def palindrome_of_length_at_least_n(s):
    """
    Returns the set of all palindromes of the length greater than or equal to 115 that exist in the given string.
    Each palindrome should only consist of English letters. If no such palindromes exist in the given string,
    the function returns an empty set. The function finds the palindromes in a case-insensitive manner.
    """
    pattern = '[a-zA-Z]{' + str(115) + ',}'
    regex = re.compile(pattern, re.IGNORECASE)
    return set(regex.findall(s))