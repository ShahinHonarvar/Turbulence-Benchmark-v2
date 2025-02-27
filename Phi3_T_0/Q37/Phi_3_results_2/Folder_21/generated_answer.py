def filter_chars(s):
    for i in range(603, 760):
        if 'Q' <= s[i] <= 'h':
            s = s.replace(s[i], '')
    return s