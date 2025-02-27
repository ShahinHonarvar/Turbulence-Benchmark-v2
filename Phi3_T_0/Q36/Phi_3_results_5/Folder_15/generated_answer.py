def filter_chars(s):
    for i in range(2, 7):
        if 'h' < s[i] < 'k':
            s = s.replace(s[i], '')
    return s