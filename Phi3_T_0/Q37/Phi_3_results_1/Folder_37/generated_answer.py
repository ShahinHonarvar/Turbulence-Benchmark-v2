def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (17 <= i <= 63 and 'O' <= c <= '^')))