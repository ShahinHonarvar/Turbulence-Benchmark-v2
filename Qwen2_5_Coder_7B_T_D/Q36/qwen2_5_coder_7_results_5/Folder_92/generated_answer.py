def filter_chars(s):
    for i in range(1, 6):
        char = chr(i + ord('a'))
        if ',' < char < 'f':
            s = s.replace(char, '')
    return s