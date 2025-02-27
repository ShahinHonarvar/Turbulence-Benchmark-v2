def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not 31 <= i < 70 or 'B' <= c <= 'v'))