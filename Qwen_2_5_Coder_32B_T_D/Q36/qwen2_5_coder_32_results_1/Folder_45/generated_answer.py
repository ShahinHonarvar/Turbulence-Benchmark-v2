def filter_chars(s):
    for char in s[81:86]:
        if '!' < char < 's':
            s = s.replace(char, '')
    return s