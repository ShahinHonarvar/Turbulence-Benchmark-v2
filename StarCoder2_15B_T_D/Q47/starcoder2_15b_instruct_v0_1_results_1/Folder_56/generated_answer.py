import re

def palindromes_of_specific_lengths(text):
    """
    Finds all palindromes of specific lengths in a given string.
    """
    substring = text[1:10]
    palindromes = set()
    for length in range(3, 8):
        pattern = re.compile('(?i)(\\\\w{%d})(?:\\\\W+(?P=1))+' % length)
        matches = pattern.findall(substring)
        palindromes.update(matches)
    return palindromes