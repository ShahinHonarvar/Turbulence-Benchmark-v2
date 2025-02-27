def filter_chars(s):
    start, end = (29, 33)
    for i in range(start, end):
        if '%' < s[i] < 'a':
            s = s.replace(s[i], '')
    return s