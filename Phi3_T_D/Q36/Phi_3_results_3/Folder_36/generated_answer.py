def filter_chars(s):
    for c in (chr(i) for i in range(ord('l') + 1, ord('t'))):
        s = s.replace(c, '')
    return s