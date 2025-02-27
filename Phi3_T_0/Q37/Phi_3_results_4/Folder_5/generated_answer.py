def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (24 <= i <= 82 and '5' <= c <= '<')])