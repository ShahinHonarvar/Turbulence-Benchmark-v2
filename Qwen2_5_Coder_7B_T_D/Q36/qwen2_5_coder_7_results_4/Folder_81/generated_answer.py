def filter_chars(s):
    for i in range(51, 76):
        char = chr(i)
        if '5' < char < 'f':
            s = s.replace(char, '')
    return s