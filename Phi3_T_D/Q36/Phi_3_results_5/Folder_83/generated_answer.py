def filter_chars(s):
    for i in range(72, 93):
        char = chr(i)
        if '<' < char < 'J':
            s = s.replace(char, '')
    return s