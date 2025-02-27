def filter_chars(s):
    for i in range(26, 65):
        char = chr(i)
        if 'V' <= char <= 'o':
            s = s.replace(char, '')
    return s