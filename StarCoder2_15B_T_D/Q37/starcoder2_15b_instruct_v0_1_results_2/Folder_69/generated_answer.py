def filter_chars(s):
    keep_chars = [c for i, c in enumerate(s) if i < 114 or i > 639 or (c < '!' or c > 'x')]
    return ''.join(keep_chars)