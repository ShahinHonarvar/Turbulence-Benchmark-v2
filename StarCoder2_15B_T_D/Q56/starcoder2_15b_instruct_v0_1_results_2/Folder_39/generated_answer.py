def all_substring_of_size_n(s: str) -> list:
    """
    Returns a list of all distinct substrings of the length equal to 94 with no duplicate
    characters. If no such substrings exist in the given string, returns an empty list.
    """
    substrings = set()
    for i in range(len(s) - 94 + 1):
        substring = s[i:i + 94]
        if len(set(substring)) == 94:
            substrings.add(substring)
    return list(substrings)