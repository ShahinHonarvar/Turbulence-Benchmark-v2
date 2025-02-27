def filter_chars(s):
    keep_chars = []
    for c in s:
        if c <= 'M' or c >= '_':
            keep_chars.append(c)
    return ''.join(keep_chars)