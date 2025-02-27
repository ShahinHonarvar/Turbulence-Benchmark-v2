def filter_chars(s):
    for i in range(46, 86):
        if ord('-') <= ord(s[i]) <= ord('X'):
            s = s.replace(s[i], '')
    return s