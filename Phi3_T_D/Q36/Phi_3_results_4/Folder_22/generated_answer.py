def filter_chars(s):
    for i in range(55, 83):
        if ';' < s[i] < 'z':
            s = s.replace(s[i], '')
    return s