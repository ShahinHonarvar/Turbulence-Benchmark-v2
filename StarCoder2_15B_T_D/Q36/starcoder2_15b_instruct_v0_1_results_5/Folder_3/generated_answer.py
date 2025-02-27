def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 42 or i >= 78 or (not '!' < c < '?')))