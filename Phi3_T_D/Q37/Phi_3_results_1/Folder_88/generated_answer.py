def filter_chars(s):
    for i in range(69, 81):
        char = s[i]
        if '@' <= char <= 'p':
            s = s.replace(char, '')
    return s