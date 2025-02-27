def all_substring_of_size_n(string):
    """
    Returns a list of all distinct substrings of length 96 with no duplicate characters in the given string.
    If no such substrings exist, an empty list is returned.
    """
    substrings = set()
    for i in range(len(string) - 95):
        substring = string[i:i + 96]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)