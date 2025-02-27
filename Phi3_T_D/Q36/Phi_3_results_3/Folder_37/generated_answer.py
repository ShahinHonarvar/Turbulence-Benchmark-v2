def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (44 < i < 59 and '/' < c < '6')))