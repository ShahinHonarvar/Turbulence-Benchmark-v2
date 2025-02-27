def filter_chars(s):
    for char in set(s[31:73]):
        if 'M' < char < 'j':
            s = s.replace(char, '')
    return s