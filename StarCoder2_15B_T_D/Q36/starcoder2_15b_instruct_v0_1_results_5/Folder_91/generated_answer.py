def filter_chars(s):
    for c in s[1:3]:
        if ord(c) > ord('$') and ord(c) < ord('?'):
            s = s.replace(c, '')
    return s