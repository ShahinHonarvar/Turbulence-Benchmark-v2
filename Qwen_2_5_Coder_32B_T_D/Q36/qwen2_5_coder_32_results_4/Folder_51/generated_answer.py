def filter_chars(s):
    t = s[58:81]
    for char in t:
        if '5' < char < '>':
            s = s.replace(char, '')
    return s