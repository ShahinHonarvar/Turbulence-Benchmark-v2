def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (10 <= i <= 69 and 'I' <= c <= 'K')))