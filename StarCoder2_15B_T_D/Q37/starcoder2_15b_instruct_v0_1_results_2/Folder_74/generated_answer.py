def filter_chars(string: str) -> str:
    """
    Removes all characters that are between indices 19 and 32, both inclusive,
    and are greater than or equal to 'f' and smaller than or equal to 'o', from
    the given string, while preserving the order of all characters in the string.
    """
    filtered_chars = [char for i, char in enumerate(string) if i < 19 or i > 32 or (ord(char) < ord('f') or ord(char) > ord('o'))]
    return ''.join(filtered_chars)