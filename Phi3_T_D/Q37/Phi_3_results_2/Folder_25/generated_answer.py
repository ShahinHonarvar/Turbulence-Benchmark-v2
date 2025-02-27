def filter_chars(s):
    for i in range(31, 39):
        char = s[i]
        if ';' <= char <= 'g':
            s = s.replace(char, '')
    return s