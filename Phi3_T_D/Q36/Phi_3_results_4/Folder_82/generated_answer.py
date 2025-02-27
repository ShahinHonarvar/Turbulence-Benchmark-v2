def filter_chars(s):
    for char in range(69, 97):
        if 'V' < char < 'j':
            s = s.replace(chr(char), '')
    return s