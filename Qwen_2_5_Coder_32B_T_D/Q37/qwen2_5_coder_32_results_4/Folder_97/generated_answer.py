def filter_chars(s):
    t = s[227:236]
    for char in set(t):
        if 'D' <= char <= 'u':
            s = s.replace(char, '')
    return s