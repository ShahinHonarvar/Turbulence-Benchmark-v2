def filter_chars(s):
    """
    Filters characters between indices 49 and 56 (both exclusive) in the given string.
    """
    filtered_chars = []
    for char in s:
        ascii_code = ord(char)
        if not 49 < ascii_code < 56:
            filtered_chars.append(char)
    return ''.join(filtered_chars)