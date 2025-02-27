def filter_chars(s):
    for i in range(51, 97):
        char = s[i]
        if 'X' <= char <= 'p':
            s = s.replace(char, '')
    return s