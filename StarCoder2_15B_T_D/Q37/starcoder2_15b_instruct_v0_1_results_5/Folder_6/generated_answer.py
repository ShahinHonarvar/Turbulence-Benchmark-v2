def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 13 or i > 28 or c < 'c' or (c > 'n')))