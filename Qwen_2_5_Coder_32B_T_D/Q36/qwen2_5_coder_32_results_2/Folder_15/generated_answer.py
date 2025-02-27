def filter_chars(s):
    t = s[2:7]
    for char in t:
        if 'h' < char < 'k':
            s = s.replace(char, '')
    return s