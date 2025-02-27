def all_substring_of_size_n(s: str) -> list:
    """
    Returns the list of all distinct substrings of the length equal to 86 with no duplicate characters.
    If no such substrings exist in the given string, returns an empty list.
    """
    result = []
    n = 86
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result