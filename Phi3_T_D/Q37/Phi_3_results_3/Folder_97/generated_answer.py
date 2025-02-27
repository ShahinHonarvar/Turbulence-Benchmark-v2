def filter_chars(s):
    for char in ' '.join([s[i] for i in range(227, 236)]):
        if 'D' <= char <= 'u':
            s = s.replace(char, '')
    return s