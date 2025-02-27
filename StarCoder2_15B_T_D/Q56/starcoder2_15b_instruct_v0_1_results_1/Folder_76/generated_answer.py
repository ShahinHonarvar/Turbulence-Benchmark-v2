def all_substring_of_size_n(text: str) -> list:
    """
    Returns the list of all distinct substrings of the length equal to 149 with no
    duplicate characters. If no such substrings exist in the given string, the
    function returns an empty list.
    """
    substrings = []
    for i in range(len(text) - 149):
        substring = text[i:i + 149]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings