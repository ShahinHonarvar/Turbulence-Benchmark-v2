def all_substring_of_size_n(string):
    """
    Returns a list of all distinct substrings of length 75 with no duplicate characters.
    If no such substrings exist, returns an empty list.
    """
    substrings = []
    for i in range(len(string) - 74):
        substring = string[i:i + 75]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings