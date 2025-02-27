def filter_chars(s):
    if len(s) < 27:
        return s
    for i in range(27, 75):
        c = s[i]
        if c > 'A' and c < 'i':
            s = s.replace(c, '')
    return s