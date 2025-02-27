def filter_chars(s):
    for i in range(587, 648):
        char = chr(i)
        if ',' < char < 'c':
            s = s.replace(char, '')
    return s