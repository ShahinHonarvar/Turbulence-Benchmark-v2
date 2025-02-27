def filter_chars(string):
    return ''.join((c for i, c in enumerate(string) if (i < 114 or i > 639) or not '!' <= c <= 'x'))