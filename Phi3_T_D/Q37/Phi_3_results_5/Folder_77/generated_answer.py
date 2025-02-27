def filter_chars(s):
    for i in range(384, 411 + 1):
        c = s[i]
        if '/' <= c <= '8':
            s = s.replace(c, '')
    return s