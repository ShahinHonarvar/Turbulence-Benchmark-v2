def filter_chars(s):
    if len(s) < 33:
        return s
    for char in s[29:33]:
        if '%' < char < 'a':
            s = s.replace(char, '')
    return s