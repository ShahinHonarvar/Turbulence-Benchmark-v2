def filter_chars(s):
    for c in s[38:81]:
        if '.' < c < '^':
            s = s.replace(c, '')
    return s