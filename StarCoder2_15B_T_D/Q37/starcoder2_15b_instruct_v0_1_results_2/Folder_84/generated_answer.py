def filter_chars(s):
    keep = []
    for c in s:
        if c < '6' or c > 'A':
            keep.append(c)
    return ''.join(keep)