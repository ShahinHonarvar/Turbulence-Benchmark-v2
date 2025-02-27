def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (57 <= i <= 96 and '<' <= c <= 'w')))