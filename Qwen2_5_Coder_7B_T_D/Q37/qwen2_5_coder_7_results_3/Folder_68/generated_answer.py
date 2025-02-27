def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (7 <= i <= 9 and '6' <= c <= 'w')))