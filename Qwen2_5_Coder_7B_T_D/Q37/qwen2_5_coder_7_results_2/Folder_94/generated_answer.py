def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (51 <= i <= 96 and 'X' <= c <= 'p')))