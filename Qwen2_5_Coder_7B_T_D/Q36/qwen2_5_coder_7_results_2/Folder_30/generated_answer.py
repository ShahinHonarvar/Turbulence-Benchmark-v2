def filter_chars(s):
    s1 = s[0:23] + s[45:]
    s2 = ''
    for c in s1:
        if not '4' <= c <= 'H':
            s2 += c
    return s2