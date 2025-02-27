def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (22 <= i <= 85 and '7' <= c <= 'e')))