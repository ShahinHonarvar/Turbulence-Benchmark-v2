def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (11 <= i <= 72 and 'i' <= c <= 'v')])