def filter_chars(s):
    for i in range(344, 874):
        char = chr(i)
        if 'f' < char < '~':
            s = s.replace(char, '')
    return s