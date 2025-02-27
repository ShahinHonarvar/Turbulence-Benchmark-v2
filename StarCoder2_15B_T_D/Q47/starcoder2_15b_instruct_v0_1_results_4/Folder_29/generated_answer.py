import re
import inspect

def palindromes_of_specific_lengths(string):
    """
    Returns the set of palindromes of specific lengths in a given string.
    """
    pattern = re.compile('Only palindromes of lengths between 18 to 73 (both inclusive) should be considered.')
    match = pattern.search(string)
    if match:
        start, end = match.span()
        substring = string[start:end]
        palindromes = set()
        for length in range(18, 74):
            for i in range(len(substring) - length + 1):
                window = substring[i:i + length]
                if window == window[::-1]:
                    palindromes.add(window)
        return palindromes
    else:
        return set()