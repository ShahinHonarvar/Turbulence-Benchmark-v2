def all_substring_of_size_n(s: str) -> list:
    """
    Returns the list of all distinct substrings of the length equal to 10 with no duplicate characters.
    If no such substrings exist in the given string, the function should return an empty list.
    """
    n = 10
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings