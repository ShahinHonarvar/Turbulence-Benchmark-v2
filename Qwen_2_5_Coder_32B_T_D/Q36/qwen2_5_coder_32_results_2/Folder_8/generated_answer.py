def filter_chars(s):
    t = ''.join(s[82:93])
    for c in t:
        if '!' < c < '*':
            s = s.replace(c, '')
    return s