import re

def palindromes_of_specific_lengths(string: str) -> set:
    """
    Finds all palindromes in a substring of the given string with specific lengths.
    Only palindromes of lengths between 21 and 31 (both inclusive) should be considered.
    Each palindrome should only consist of English letters. The function should
    find the palindromes in a case-insensitive manner.
    """
    substring = string[24:85]
    pattern = re.compile('([a-zA-Z]{21,31})(?=\\\\1)', re.IGNORECASE)
    return set(re.findall(pattern, substring))