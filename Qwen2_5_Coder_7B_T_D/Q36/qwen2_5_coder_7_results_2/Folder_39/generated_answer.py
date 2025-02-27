def filter_chars(s):
    for char in set(s[43:59]):
        if '6' < char < 'C':
            s = s.replace(char, '')
    return s