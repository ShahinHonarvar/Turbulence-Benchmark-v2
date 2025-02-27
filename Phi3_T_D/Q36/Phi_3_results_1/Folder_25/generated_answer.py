def filter_chars(s):
    altered_str = ''.join([c for i, c in enumerate(s) if i not in range(24, 37) or 'A' <= c <= 'h'])
    return altered_str