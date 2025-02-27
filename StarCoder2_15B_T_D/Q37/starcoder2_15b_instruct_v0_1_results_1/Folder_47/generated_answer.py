def filter_chars(s):
    """
    Filter out characters between indices 38 and 54, both inclusive,
    and greater than or equal to ':' and smaller than or equal to 'r'.
    """
    filtered_chars = [c for i, c in enumerate(s) if i < 38 or i > 54 or (c < ':' or c > 'r')]
    return ''.join(filtered_chars)