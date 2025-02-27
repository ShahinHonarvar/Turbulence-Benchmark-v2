def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 72 or i > 94 or c < '.' or (c > 'b')))