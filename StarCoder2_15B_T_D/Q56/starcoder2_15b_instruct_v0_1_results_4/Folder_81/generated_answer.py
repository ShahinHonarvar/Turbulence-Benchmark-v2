import itertools

def all_substring_of_size_n(string):
    """
    Returns the list of all distinct substrings of the length equal to 98 with no duplicate characters.
    If no such substrings exist, returns an empty list.
    """
    substrings = []
    for i in range(len(string) - 98 + 1):
        substring = string[i:i + 98]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings