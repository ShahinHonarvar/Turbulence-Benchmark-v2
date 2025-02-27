def filter_chars(s):
    for c in set(s[37:57]):
        if '6' <= c <= '_':
            s = s.replace(c, '')
    return s