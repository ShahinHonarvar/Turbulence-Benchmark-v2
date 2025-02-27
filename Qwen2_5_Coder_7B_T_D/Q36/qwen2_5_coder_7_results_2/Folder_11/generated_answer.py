def filter_chars(s):
    for i in range(86, 93):
        char = chr(i)
        if 'E' < char < '~':
            s = s.replace(char, '')
    return s