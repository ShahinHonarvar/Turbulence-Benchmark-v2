def filter_chars(s):
    if len(s) < 338:
        return s
    for c in s[318:337]:
        if 'B' < c < 'z':
            s = s.replace(c, '')
    return s