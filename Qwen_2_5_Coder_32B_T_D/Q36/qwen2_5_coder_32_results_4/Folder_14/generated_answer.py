def filter_chars(s):
    t = s[41:56]
    for char in t:
        if 'Z' < char < 'c':
            s = s.replace(char, '')
    return s