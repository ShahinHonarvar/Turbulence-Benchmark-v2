def filter_chars(s):
    return ''.join([ch for i, ch in enumerate(s) if (i < 57 or i > 96) or (ch < '<' or ch > 'w')])