def filter_chars(s):
    for i in range(344, 665):
        char = chr(i)
        if '%' < char < 'U':
            s = s.replace(char, '')
    return s