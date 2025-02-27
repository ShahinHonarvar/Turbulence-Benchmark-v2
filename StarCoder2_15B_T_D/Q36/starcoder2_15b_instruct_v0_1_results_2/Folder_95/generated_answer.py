def filter_chars(string):
    for i in range(56, 86):
        if chr(i) > '+' and chr(i) < 'w':
            string = string.replace(chr(i), '')
    return string