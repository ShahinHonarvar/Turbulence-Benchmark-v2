def filter_chars(s):
    for i in range(603, 760):
        char = s[i]
        if 'Q' <= char <= 'h':
            s = s.replace(char, '')
    return s