def filter_chars(s):
    for i in range(43, 69):
        char = chr(i)
        if 'B' < char < 'r':
            s = s.replace(char, '')
    return s