def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 29 or i > 79 or (not 'k' <= c <= 'z')))