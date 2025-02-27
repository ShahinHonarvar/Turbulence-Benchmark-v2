def filter_chars(s):
    for index in range(55, 66):
        if 'f' < s[index] < '|':
            s = s.replace(s[index], '')
    return s