def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (44 < i < 68 and 'W' < c < 'x')))