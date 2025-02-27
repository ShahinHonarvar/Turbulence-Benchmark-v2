def all_substring_of_size_n(string: str) -> list:
    """
    Returns all distinct substrings of length 37 with no duplicate characters in the given string.
    If no such substrings exist, returns an empty list.
    """
    if len(string) < 37:
        return []
    substrings = set()
    for i in range(len(string) - 36):
        substring = string[i:i + 37]
        if len(set(substring)) == 37:
            substrings.add(substring)
    return list(substrings)