def filter_chars(s):
    for i in range(40, 62):
        if '8' > s[i] > 'h':
            s = s.replace(s[i], '')
    return s