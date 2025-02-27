def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (20 <= i <= 62 and 'i' <= c <= 'k')))