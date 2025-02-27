def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (75 <= i <= 99 and '8' <= c <= 'e')))