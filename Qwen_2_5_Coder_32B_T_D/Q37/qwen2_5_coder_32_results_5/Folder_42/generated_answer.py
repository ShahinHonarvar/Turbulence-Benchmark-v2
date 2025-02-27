def filter_chars(s):
    for char in s[73:75]:
        if 'U' <= char <= 'l':
            s = s.replace(char, '')
    return s