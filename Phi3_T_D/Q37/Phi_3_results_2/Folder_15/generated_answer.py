def filter_chars(s):
    for c in ''.join(set(s[2:7])):
        if '?' <= c <= 'f':
            s = s.replace(c, '')
    return s[2:7] + s[:2] + s[7:]