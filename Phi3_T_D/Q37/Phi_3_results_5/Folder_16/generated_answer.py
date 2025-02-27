def filter_chars(s):
    for i in range(225, 382):
        char = s[i]
        if 'D' <= char <= 'Y':
            s = s.replace(char, '')
    return s