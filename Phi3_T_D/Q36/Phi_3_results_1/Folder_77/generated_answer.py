def filter_chars(s):
    for i in range(221, 420):
        if '-' < s[i] < 'v':
            s = s.replace(s[i], '')
    return s