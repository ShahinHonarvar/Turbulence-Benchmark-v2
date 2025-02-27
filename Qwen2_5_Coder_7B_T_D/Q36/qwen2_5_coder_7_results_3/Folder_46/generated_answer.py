def filter_chars(s):
    for i in range(19, 69):
        if 'C' > s[i] > '<':
            s = s.replace(s[i], '')
    return s