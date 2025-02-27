def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not 34 <= i <= 67 or not 'W' <= c <= 'x'))