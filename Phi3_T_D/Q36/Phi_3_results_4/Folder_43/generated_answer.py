def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not 27 < i < 75 or not 'A' < c < 'i'))