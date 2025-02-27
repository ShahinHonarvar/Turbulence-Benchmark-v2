def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 7 or i > 8 or c < 'B' or (c > 'H')))