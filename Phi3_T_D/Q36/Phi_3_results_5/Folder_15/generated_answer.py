def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not 2 < i < 7 or 'h' < c < 'k'))