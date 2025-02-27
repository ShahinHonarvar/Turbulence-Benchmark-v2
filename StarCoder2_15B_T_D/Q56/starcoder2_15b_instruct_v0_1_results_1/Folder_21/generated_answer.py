def all_substring_of_size_n(string):
    """
    This function takes a string as an argument and returns a list of all distinct
    substrings of length 106 with no duplicate characters. If no such substrings exist,
    the function returns an empty list.
    """
    substrings = []
    for i in range(len(string) - 106 + 1):
        substring = string[i:i + 106]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings