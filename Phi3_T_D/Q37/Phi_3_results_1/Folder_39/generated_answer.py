def filter_chars(s):
    for i in range(52, 82):
        char = chr(i)
        if 'A' <= char <= 'U':
            s = s.replace(char, '')
    return s