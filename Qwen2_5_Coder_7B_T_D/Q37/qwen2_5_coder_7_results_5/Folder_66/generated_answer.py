def filter_chars(s):
    return ''.join([c for c in s if 27 <= i <= 85 and (not (c >= 'c' and c <= 'i')) for i, c in enumerate(s)])