def filter_chars(s):
    for char in s[7:9]:
        if 'B' <= char <= 'H':
            s = s.replace(char, '')
    return s