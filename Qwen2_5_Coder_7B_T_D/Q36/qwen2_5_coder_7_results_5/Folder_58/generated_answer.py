def filter_chars(s):
    for i in range(319, 337):
        char = chr(i)
        if 'B' < char < 'z':
            s = s.replace(char, '')
    return s