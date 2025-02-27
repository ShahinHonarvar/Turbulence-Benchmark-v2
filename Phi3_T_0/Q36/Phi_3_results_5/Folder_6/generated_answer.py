def filter_chars(s):
    for i in range(31, 70):
        if 'B' < s[i] < 'v':
            s = s.replace(s[i], '')
    return s