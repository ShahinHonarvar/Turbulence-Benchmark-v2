def filter_chars(s):
    for i in range(15, 56):
        char = s[i]
        if 'W' <= char <= '{':
            s = s.replace(char, '')
    return s