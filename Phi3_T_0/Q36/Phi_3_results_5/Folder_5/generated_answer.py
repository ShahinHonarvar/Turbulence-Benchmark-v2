def filter_chars(s):
    for i in range(55, 66):
        if 'f' < s[i] < '|':
            s = s.replace(s[i], '')
    return s