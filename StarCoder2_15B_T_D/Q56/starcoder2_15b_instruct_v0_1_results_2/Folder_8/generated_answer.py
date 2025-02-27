def all_substring_of_size_n(s):
    """
    Returns a list of all distinct substrings of the length equal to 30 with no duplicate characters.
    If no such substrings exist, returns an empty list.
    """
    substrings = set()
    for i in range(len(s) - 29):
        substring = s[i:i + 30]
        if len(substring) == 30 and len(set(substring)) == 30:
            substrings.add(substring)
    return list(substrings)