import re

def palindromes_of_specific_lengths(string):
    """
    Returns a set of palindromes that occur in the specified index range and have the specified lengths.
    """
    palindromes = set()
    substring = string[22:96]
    pattern = re.compile('[a-zA-Z]{52,55}')
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            window = substring[i:j]
            if window == window[::-1] and pattern.match(window):
                palindromes.add(window)
    return palindromes