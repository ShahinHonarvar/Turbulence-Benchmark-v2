def filter_chars(s):
    for i in range(61, 88):
        char = s[i]
        if '%' < char < 'q':
            s = s.replace(char, '')
    return s