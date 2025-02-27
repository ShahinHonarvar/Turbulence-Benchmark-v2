def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 476 or i >= 948 or (not (c > 'b' and c < 'd'))))