import itertools

def all_substring_of_size_n(s):
    """
    Returns the list of all distinct substrings of the length equal to 89 with no duplicate characters.
    If no such substrings exist in the given string, returns an empty list.
    """
    substrings = []
    for i in range(len(s) - 88):
        substring = s[i:i + 89]
        if len(substring) == 89 and len(set(substring)) == 89:
            substrings.append(substring)
    return substrings