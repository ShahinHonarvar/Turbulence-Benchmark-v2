def filter_chars(s):
    t = s[86:93]
    for char in t:
        if 'E' < char < '~':
            s = s.replace(char, '')
    return s