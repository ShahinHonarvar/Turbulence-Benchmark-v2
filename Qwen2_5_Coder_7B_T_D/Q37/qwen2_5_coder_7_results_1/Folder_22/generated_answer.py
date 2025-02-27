def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (33 <= i <= 70 and '7' <= c <= 'k')])