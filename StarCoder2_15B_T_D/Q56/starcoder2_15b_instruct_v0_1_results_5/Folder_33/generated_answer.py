def all_substring_of_size_n(string):
    """Return the list of all distinct substrings of the length equal to 105 with no duplicate characters."""
    substrings = []
    for i in range(len(string) - 105 + 1):
        substring = string[i:i + 105]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings