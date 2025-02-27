def all_substring_of_size_n(string: str) -> list:
    """
    Returns the list of all distinct substrings of the length equal to 31 with no duplicate characters.
    If no such substrings exist, returns an empty list.
    """
    substrings = []
    n = 31
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings