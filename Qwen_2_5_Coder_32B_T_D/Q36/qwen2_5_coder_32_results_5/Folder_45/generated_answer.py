def filter_chars(s):
    t = s[81:86]
    for char in t:
        if '!' < char < 's':
            s = s.replace(char, '')
    return s