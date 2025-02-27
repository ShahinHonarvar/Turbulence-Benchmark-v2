def filter_chars(s):
    altered_s = ''.join((c for i, c in enumerate(s) if not 34 <= i <= 67 or not 'W' <= c <= 'x'))
    return altered_s