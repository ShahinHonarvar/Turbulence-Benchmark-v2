def filter_chars(s):
    for i in range(37, 57):
        char = s[i]
        if '6' <= char <= '_':
            s = s.replace(char, '')
    return s