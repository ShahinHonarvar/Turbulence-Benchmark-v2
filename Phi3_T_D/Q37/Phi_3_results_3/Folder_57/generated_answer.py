def filter_chars(s):
    return ''.join((c for i, c in enumerate(s, start=1) if not (27 <= i <= 85 and '!' <= c <= 'B')))