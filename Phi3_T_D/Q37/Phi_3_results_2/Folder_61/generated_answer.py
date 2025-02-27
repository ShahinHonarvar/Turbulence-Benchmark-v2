def filter_chars(s):
    for i in range(5, 7):
        char = s[i]
        if 'G' <= char <= 'p':
            s = s.replace(char, '')
    return s