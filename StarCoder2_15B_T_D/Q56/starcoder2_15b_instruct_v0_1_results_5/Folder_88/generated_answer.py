def all_substring_of_size_n(s: str) -> [str]:
    """
    Returns the list of all distinct substrings of length 68 with no duplicate characters.
    If no such substrings exist, returns an empty list.
    """
    n = 68
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings