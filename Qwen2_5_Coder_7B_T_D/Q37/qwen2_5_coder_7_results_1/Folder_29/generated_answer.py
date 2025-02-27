def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if (i < 12 or i > 88) or not '&' <= c <= 'v'))