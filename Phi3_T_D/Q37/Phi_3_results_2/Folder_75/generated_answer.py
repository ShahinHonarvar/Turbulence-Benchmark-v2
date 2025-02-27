def filter_chars(s):
    start, end = (34, 67)
    for i in range(start, end + 1):
        if 'W' <= s[i] <= 'x':
            s = s.replace(s[i], '')
    return s