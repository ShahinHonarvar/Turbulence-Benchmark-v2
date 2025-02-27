def all_substring_of_size_n(string):
    """
    Returns all distinct substrings of length 96 with no duplicate characters in `string`.
    If no such substrings exist, returns an empty list.
    """
    substrings = []
    length_of_string = len(string)
    for i in range(length_of_string - 96 + 1):
        substring = string[i:i + 96]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings