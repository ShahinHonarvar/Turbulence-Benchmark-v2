def filter_chars(s):
    start, end = (54, 92)
    for i in range(start, end):
        c = s[i]
        if 'J' < c < 'X':
            s = s.replace(c, '')
    return s