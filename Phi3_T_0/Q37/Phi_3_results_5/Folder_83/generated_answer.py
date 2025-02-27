def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (29 <= i <= 79 and 'K' <= c <= 'z')))