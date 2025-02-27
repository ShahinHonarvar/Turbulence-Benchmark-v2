def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (42 <= i <= 92 and '/' <= c <= 'a')))