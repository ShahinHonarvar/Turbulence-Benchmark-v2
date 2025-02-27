def filter_chars(string: str) -> str:
    """
    Removes all occurrences of a specific character within a string.
    """
    filtered_chars = []
    for char in string:
        if not (char > ';' and char < 'r'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)