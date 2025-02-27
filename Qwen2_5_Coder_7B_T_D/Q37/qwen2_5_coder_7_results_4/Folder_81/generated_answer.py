def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (19 <= i <= 92 and '8' <= c <= 'm')))