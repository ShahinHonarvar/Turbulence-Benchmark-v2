def filter_chars(s):
    return ''.join((c for i, c in enumerate(s, 1) if not (38 <= i <= 99 and 'A' <= c <= 'Q')))