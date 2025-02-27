def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 11 or i >= 46 or (not (c > '!' and c < 'A'))))