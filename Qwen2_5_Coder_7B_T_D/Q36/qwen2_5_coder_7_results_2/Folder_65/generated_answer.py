def filter_chars(s):
    for i in range(58, 82):
        char = chr(i)
        if 'F' < char < 'O':
            s = s.replace(char, '')
    return s