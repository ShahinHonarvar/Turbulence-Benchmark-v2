def filter_chars(s):
    for i in range(46, 74):
        if '&' < s[i] < 'M':
            s = s.replace(s[i], '')
    return s