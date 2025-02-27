def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (154 < i < 222 and 'A' < c < 'f')))