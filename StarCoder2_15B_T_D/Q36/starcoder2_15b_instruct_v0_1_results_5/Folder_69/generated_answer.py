def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 343 or i >= 665 or (not '%' < c < 'U')))