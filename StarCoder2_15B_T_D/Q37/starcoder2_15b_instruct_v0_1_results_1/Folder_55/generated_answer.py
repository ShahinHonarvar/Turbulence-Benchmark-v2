def filter_chars(string: str) -> str:
    """
    Filter characters between indices 1 and 5 (inclusive) that are greater than or equal to
    '$' and smaller than or equal to ';' from a given string.
    """
    filtered_chars = []
    for i, c in enumerate(string):
        if i >= 1 and i <= 5 and (ord(c) >= ord('$')) and (ord(c) <= ord(';')):
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)