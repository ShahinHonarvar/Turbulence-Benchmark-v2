def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (114 <= i <= 639 and '!' <= c <= 'x')))