def filter_chars(s):
    for index in range(41, 87):
        char = s[index]
        if 'S' <= char <= 's':
            s = s.replace(char, '')
    return s