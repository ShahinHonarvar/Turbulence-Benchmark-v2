def filter_chars(s):
    """
    Filter characters between indices 13 and 28, inclusive, that are between 'c' and 'n', exclusive.
    """
    filtered_chars = []
    for i, c in enumerate(s):
        if 13 <= i <= 28 and ord('c') <= ord(c) < ord('n'):
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)