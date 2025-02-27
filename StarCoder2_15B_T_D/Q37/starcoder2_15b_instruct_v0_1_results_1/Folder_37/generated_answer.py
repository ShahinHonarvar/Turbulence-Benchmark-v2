def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 17 or i > 63 or c < 'O' or (c > '^')])