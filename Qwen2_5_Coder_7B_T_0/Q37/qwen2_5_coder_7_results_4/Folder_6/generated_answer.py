def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (13 <= i <= 28 and 'c' <= c <= 'n')))