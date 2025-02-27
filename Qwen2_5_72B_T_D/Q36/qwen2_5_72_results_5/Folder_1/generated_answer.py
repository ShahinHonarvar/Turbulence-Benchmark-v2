def filter_chars(s):
    for c in set(s[69:87]):
        if '#' < c < 'L':
            s = s.replace(c, '')
    return s