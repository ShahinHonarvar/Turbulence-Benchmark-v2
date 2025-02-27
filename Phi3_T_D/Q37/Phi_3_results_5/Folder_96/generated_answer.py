def filter_chars(s):
    indices = range(86, 93)
    for index in indices:
        char = s[index]
        if '!' <= char <= 's':
            s = s.replace(char, '')
    return s