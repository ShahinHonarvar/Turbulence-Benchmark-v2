def filter_chars(s):
    for char in s[46:91]:
        if 'D' < char < 'H':
            s = s.replace(char, '')
    return s