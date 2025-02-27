def filter_chars(s):
    for i in range(503, 754):
        char = s[i]
        if '9' <= char <= 'w':
            s = s.replace(char, '')
    return s