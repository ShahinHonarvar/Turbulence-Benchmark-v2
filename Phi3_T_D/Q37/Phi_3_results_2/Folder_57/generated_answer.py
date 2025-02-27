def filter_chars(string):
    for i in range(27, 86):
        char = chr(i)
        if '!' <= char <= 'B':
            string = string.replace(char, '')
    return string