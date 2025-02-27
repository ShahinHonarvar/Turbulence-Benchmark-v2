def filter_chars(s: str) -> str:
    """
    Filters characters from a string based on their position and value.

    Args:
        s (str): The input string.

    Returns:
        str: The filtered string.
    """
    filtered = ''
    for i, c in enumerate(s):
        if not (4 <= i <= 4 and '7' <= c <= 'o'):
            filtered += c
    return filtered