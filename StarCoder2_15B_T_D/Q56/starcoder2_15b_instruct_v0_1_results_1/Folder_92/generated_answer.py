def all_substring_of_size_n(string):
    """
    Returns the list of all distinct substrings of the length equal to 9 with no duplicate characters.
    If no such substrings exist in the given string, the function returns an empty list.
    """
    substrings = []
    for i in range(len(string) - 8):
        substring = string[i:i + 9]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings