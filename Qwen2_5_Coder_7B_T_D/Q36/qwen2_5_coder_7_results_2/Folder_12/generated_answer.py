def filter_chars(s):
    for char in s[32:84]:
        if 'm' < char < 'w':
            s = s.replace(char, '')
    return s