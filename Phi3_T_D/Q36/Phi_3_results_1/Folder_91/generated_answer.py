def filter_chars(s):
    for i in range(4):
        if ord('$') < ord(s[i]) < ord('?'):
            s = s.replace(s[i], '')
    return s