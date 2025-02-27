import re

def palindromes_of_specific_lengths(string):
    """
    Returns the set of all palindromes in the given string that satisfy the following conditions:
    1. The palindromes should only consist of English letters.
    2. The palindromes should be of lengths between 13 and 66.
    3. The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    substring = string[11:84]
    for length in range(13, 67):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window == window[::-1] and re.match('^[a-zA-Z]+$', window):
                palindromes.add(window)
    return palindromes