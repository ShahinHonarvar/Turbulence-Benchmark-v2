def filter_chars(s):
    for i in range(43, 68):
        if 'B' < s[i] < 'r':
            s = s.replace(s[i], '')
    return s