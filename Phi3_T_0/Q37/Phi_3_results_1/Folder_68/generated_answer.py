def filter_chars(s):
    for i in range(7, 10):
        if '6' <= s[i] <= 'w':
            s = s.replace(s[i], '')
    return s