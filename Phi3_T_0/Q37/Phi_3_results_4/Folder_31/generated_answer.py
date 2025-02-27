def filter_chars(s):
    for i in range(57, 97):
        if '<' <= chr(i) <= 'w':
            s = s.replace(chr(i), '')
    return s