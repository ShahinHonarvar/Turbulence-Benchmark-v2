def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (26 <= i <= 64 and 'V' <= c <= 'o')))