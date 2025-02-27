def filter_chars(s):
    for i in range(35, 90):
        char = chr(i)
        if 'E' <= char <= 't':
            s = s.replace(char, '')
    return s