def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (10 <= i <= 52 and '@' <= c <= 'T')))