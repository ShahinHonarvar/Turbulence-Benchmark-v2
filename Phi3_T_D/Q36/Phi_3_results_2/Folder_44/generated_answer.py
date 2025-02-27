def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if (i < 18 or i >= 64) or not '3' < c < 'B'))