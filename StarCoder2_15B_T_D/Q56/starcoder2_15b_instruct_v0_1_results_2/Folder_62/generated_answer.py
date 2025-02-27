def all_substring_of_size_n(s):
    """
    Returns a list of all distinct substrings of the length 32 with no duplicate characters.
    """
    substrings = []
    n = 32
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings