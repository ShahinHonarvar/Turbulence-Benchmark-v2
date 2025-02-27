def all_substring_of_size_n(string: str) -> list:
    """
    Returns the list of all distinct substrings of the length equal to 8 with no duplicate characters.
    If no such substrings exist in the given string, the function should return an empty list.
    """
    result = []
    n = 8
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result