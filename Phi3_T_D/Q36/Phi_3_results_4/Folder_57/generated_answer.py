def filter_chars(s):
    for i in range(70, 75):
        if 'A' < s[i] < 'U':
            s = s.replace(s[i], '')
    return s