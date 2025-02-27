def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (35 <= i <= 98 or 'A' <= c <= 'b')])