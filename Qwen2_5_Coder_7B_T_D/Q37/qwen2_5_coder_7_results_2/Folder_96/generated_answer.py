def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (86 <= i <= 92 and '!' <= c <= 's')))