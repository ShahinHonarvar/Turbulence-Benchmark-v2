def filter_chars(s):
    for i in range(35, 52):
        c = s[i]
        if c >= 'H' and c <= 's':
            s = s.replace(c, '')
    return s