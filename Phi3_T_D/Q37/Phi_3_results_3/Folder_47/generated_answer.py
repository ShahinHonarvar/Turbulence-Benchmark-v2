def filter_chars(s):
    for i in range(38, 55):
        c = s[i]
        if ':' <= c <= 'r':
            s = s.replace(c, '')
    return s