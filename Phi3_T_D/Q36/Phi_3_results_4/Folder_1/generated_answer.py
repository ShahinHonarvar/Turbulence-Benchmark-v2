def filter_chars(s):
    for c in s[69:87]:
        if '#' < c < 'L':
            s = s.replace(c, '')
    return s