def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (69 <= i <= 80 and '@' <= c <= 'p')))