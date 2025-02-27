def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (8 <= i <= 9 and 'R' <= c <= 't')))