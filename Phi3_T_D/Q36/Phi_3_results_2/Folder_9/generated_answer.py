def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 50 or i >= 92 or (not 'A' < c < 'Q')])