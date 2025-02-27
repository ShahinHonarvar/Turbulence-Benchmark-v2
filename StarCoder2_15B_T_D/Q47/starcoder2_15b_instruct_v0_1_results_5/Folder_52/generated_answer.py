import re

def palindromes_of_specific_lengths(string):
    """
    Find all palindromes of specific lengths in a given string.
    Only palindromes of lengths between 13 and 42 (both inclusive)
    should be considered. Each palindrome should only consist of
    English letters. The palindromes should be found in a
    case-insensitive manner.
    """
    pattern = '[a-zA-Z]{' + str(13) + ',' + str(42) + '}'
    palindromes = set(re.findall(pattern, string[44:100], re.IGNORECASE))
    return palindromes