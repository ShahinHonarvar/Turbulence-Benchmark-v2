def all_substring_of_size_n(s):
    """
    Returns a list of all distinct substrings of length 73 with no duplicate characters in the given string `s`.
    If no such substrings exist, returns an empty list.
    """
    n = 73
    if len(s) < n:
        return []
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return substrings