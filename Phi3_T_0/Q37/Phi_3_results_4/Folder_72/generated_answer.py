def filter_chars(s):
    for i in range(35, 52):
        char = s[i]
        if 'H' <= char <= 's':
            s = s.replace(char, '')
    return s