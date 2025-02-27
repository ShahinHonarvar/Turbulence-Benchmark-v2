def filter_chars(s):
    """
    Filter characters between indices 36 and 40, inclusive, that are greater than or
    equal to 'H' and smaller than or equal to 'e'.
    """
    filtered = [c for c in s if c < 'H' or c > 'e']
    return ''.join(filtered)