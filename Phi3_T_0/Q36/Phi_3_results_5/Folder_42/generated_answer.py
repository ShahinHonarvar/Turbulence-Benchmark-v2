def filter_chars(s):
    for i in range(42, 68):
        if 't' < s[i] < 'x':
            s = s.replace(s[i], '')
    return s