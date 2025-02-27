def filter_chars(s):
    for i in range(32, 50):
        char = chr(i)
        if '/' < char < 'J':
            s = s.replace(char, '')
    return s