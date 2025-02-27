def filter_chars(s):
    start, end = (18, 64)
    for i in range(start, end):
        if '3' < s[i] < 'B':
            s = s.replace(s[i], '')
    return s