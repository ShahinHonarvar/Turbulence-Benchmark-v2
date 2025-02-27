def filter_chars(s):
    for c in list(s[54:92]):
        if 'J' < c < 'X':
            s = s.replace(c, '')
    return s