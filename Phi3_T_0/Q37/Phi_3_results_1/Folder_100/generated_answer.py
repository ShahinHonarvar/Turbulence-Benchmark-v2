def filter_chars(s):
    for i in range(88, 91):
        char = s[i]
        if 'J' <= char <= 'Q':
            s = s.replace(char, '')
    return s