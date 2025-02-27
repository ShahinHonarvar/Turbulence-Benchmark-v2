def filter_chars(s):
    for i in range(29, 33):
        char = s[i]
        if '%' < char < 'a':
            s = s.replace(char, '')
    return s