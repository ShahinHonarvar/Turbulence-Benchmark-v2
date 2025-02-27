def filter_chars(s):
    for i in range(71, 97):
        c = chr(i)
        if '_' <= c <= 'o':
            s = s.replace(c, '')
    return s