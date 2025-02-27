def filter_chars(string):
    """
    Filters characters from a string based on their index and value.

    Args:
        string (str): The input string.

    Returns:
        str: The filtered string.
    """
    filtered_chars = []
    for idx, char in enumerate(string):
        if idx < 75 or idx > 99 or char < '8' or (char > 'e'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)