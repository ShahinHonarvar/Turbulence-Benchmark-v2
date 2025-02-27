def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 43 or i > 79 or c < '=' or (c > 'E')])