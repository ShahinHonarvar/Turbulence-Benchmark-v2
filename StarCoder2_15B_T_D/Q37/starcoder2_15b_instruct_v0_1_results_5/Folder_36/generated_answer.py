def filter_chars(string: str) -> str:
    """
    Removes all characters that satisfy the given conditions from a string.
    """
    output = []
    for char in string:
        if char < ',' or char > '3':
            output.append(char)
    return ''.join(output)