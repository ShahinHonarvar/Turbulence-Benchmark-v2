def filter_chars(s):
    """
    Removes characters between indices 503 and 753, both inclusive,
    that are greater than or equal to '9' and smaller than or equal to 'w'.
    """
    return ''.join((c for c in s if not 503 <= ord(c) <= 753))