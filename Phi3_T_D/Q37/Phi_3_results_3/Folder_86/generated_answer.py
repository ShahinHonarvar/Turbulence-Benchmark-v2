def filter_chars(s):
    for i in range(164, 707):
        c = s[i]
        if 'O' <= c <= '}':
            s = s.replace(c, '')
    return s