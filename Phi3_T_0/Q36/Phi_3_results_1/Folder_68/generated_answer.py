def filter_chars(s):
    for i in range(1, 9):
        if '8' < s[i] < 'm':
            s = s.replace(s[i], '')
    return s