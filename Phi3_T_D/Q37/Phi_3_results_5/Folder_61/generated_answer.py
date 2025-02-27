def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (5 <= i <= 6 and 'G' <= c <= 'p')))