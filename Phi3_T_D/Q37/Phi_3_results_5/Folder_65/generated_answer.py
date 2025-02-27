def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 61 or i > 69 or '0' <= c <= '@'])