def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (42 <= i <= 97 and '*' <= c <= 'b')))