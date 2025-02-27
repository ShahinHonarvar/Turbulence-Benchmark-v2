def is_distinct(s: str) -> bool:
    """
    Checks if a substring has no duplicate characters.
    """
    return len(s) == len(set(s))

def all_substring_of_size_n(s: str) -> list:
    """
    Returns the list of all distinct substrings of the length equal to 27 with no duplicate characters.
    """
    n = 27
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_distinct(substring):
            result.append(substring)
    return result