def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 38 or i > 99 or 'A' <= c <= 'Q'))