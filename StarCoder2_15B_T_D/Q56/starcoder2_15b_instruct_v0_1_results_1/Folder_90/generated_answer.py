def all_substring_of_size_n(s: str) -> list:
    """
    Returns all distinct substrings of the length equal to 130 with no duplicate characters in the given string.
    If no such substrings exist, returns an empty list.
    """
    substrings = []
    for i in range(len(s) - 129):
        substring = s[i:i + 130]
        if len(set(substring)) == 130:
            substrings.append(substring)
    return substrings