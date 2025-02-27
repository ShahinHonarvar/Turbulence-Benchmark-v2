def all_substring_of_size_n(string):
    """
    Returns the list of all distinct substrings of the length equal to 57 with no duplicate characters.
    If no such substrings exist in the given string, returns an empty list.
    """
    n = 57
    substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings