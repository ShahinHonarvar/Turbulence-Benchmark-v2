import itertools

def all_substring_of_size_n(text):
    """
    Returns the list of all distinct substrings of the length equal to 55 with no duplicate characters.
    If no such substrings exist in the given string, returns an empty list.
    """
    substrings = []
    for i in range(len(text) - 54):
        substring = text[i:i + 55]
        if len(set(substring)) == 55:
            substrings.append(substring)
    return substrings