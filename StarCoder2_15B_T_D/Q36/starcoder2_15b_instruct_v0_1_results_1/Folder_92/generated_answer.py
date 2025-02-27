def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 1 or i >= 6 or (not ',' < c < 'f')))