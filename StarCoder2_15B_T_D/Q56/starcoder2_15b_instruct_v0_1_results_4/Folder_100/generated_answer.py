def all_substring_of_size_n(s):
    """
    Returns a list of all distinct substrings of length 92 with no duplicate characters in a given string.
    If no such substrings exist, returns an empty list.
    """
    n = 92
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings