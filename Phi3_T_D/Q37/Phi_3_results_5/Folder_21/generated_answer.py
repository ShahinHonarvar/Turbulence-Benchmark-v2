def filter_chars(s):
    start, end = (603, 759)
    for i in range(start, end + 1):
        char = s[i]
        if 'Q' <= char <= 'h':
            s = s.replace(char, '')
    return s