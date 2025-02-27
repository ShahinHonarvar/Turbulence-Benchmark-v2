def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 114 or i > 639 or '!' <= c <= 'x'))