def filter_chars(s):
    for i in range(11, 33):
        char = s[i]
        if '!' <= char <= '@':
            s = s.replace(char, '')
    return s