def filter_chars(string):
    return ''.join((c for i, c in enumerate(string) if i < 41 or i >= 56 or c <= 'Z' or (c >= 'c')))