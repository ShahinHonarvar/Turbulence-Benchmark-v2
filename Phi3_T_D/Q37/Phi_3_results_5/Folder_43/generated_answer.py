def filter_chars(s):
    for i in range(15, min(56, len(s))):
        char = s[i]
        if 'W' <= char <= '{':
            s = s.replace(char, '')
    return s