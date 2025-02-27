def filter_chars(s):
    for i in range(44, 48):
        if '+' < s[i] < 'l':
            s = s.replace(s[i], '')
    return s