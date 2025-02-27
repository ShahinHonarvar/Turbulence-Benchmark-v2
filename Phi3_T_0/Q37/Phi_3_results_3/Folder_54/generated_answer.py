def filter_chars(s):
    for i in range(46, 86):
        if '-' <= s[i] <= 'X':
            s = s.replace(s[i], '')
    return s