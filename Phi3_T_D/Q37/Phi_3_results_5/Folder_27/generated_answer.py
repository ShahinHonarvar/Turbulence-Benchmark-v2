def filter_chars(s):
    for i in range(43, 81):
        c = s[i]
        if '=' <= c <= 'E':
            s = s.replace(c, '')
    return s