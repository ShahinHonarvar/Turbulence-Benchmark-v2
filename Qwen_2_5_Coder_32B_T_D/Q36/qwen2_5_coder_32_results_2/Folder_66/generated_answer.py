def filter_chars(s):
    t = s[39:87]
    for char in t:
        if '!' < char < '}':
            s = s.replace(char, '')
    return s