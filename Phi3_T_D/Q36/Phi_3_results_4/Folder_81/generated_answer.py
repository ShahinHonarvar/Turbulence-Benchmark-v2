def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 51 or i >= 76 or '5' <= c <= 'f'])