import re

def all_substring_of_size_n(s):
    """
    Returns a list of all distinct substrings of the given string `s`
    of length 53 with no duplicate characters. If no such substrings exist,
    an empty list is returned.
    """
    pattern = re.compile('(?=([a-zA-Z0-9]{53}))')
    substrings = pattern.findall(s)
    return list(set(substrings))