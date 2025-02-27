def filter_chars(s):
    for i in range(57, 69):
        char = chr(i)
        if '(' < char < 'W':
            s = s.replace(char, '')
    return s