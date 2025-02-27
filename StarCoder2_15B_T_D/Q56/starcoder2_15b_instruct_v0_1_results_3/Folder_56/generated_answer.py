def all_substring_of_size_n(string):
    """
    Returns a list of all distinct substrings of the length equal to 69
    with no duplicate characters. If no such substrings exist, returns an empty list.
    """
    length = len(string)
    substrings = []
    for i in range(length - 68):
        substring = string[i:i + 69]
        if len(substring) == 69 and len(set(substring)) == 69:
            substrings.append(substring)
    return substrings